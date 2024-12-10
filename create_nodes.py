from neo4j import GraphDatabase # type: ignore
from dotenv import load_dotenv # type: ignore
import os
import time
import requests

load_dotenv()

class Neo4jConnection:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def query(self, query, parameters=None):
        with self._driver.session() as session:
            result = session.run(query, parameters)
            data = [record.data() for record in result]
            return data


uri = os.getenv("NEO4J_URI")
username = os.getenv("NEO4J_USERNAME")
password = os.getenv("NEO4J_PASSWORD")

conn = Neo4jConnection(uri, username, password)

csv_file_urls = []
with open("urls.txt", "r") as url_file:
    urls = url_file.readlines()
    csv_file_urls = [url.replace("\n", "") for url in urls]
try:
    maps = {}
    for csv_file_url in csv_file_urls:
        print(f"Processing: {csv_file_url}")
        print("URL:\n", csv_file_url)
        response = requests.get(csv_file_url)
        
        if response.status_code != 200:
            print(f"Failed to download {csv_file_url}: {response.status_code}")
            continue

        lines = response.text.splitlines()
        headers = lines[0].split(',')
        name = csv_file_url.split("/")[-1][:-4]
        primary_key = headers[0]
        try:
            set_clause = ', '.join([f"{name}.{header.strip()} = row.{header.strip()}" for header in headers])
            cypher_query = f"""
            LOAD CSV WITH HEADERS FROM '{csv_file_url}' AS row
            MERGE ({name}:{name.capitalize()} {{{primary_key}: row.{primary_key}}})
            ON CREATE SET {set_clause}
            RETURN {name}
            """
            results = conn.query(cypher_query)
            print(f"Data imported successfully from {csv_file_url}. Preview:")
            time.sleep(2)
        except Exception as e:
            with open("error.txt", "w") as file:
                file.write(csv_file_url)
            print(e)
            print("Failed url:\n", csv_file_url)
            continue

except Exception as e:
    print(f"Error: {e}")


finally:
    conn.close()
