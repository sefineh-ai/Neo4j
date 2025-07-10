from neo4j import GraphDatabase
from dotenv import load_dotenv
import os
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
csv_file_url = "https://raw.githubusercontent.com/sefineh-ai/Neo4j/main/data/accountant.csv"
csv_file_url="https://raw.githubusercontent.com/sefineh-ai/Neo4j/refs/heads/main/data/company.csv"
csv_file_url="https://raw.githubusercontent.com/sefineh-ai/Neo4j/refs/heads/main/data/profile.csv"
csv_file_url="https://raw.githubusercontent.com/sefineh-ai/Neo4j/refs/heads/main/data/product.csv"
csv_file_url="https://raw.githubusercontent.com/sefineh-ai/Neo4j/refs/heads/main/data/client.csv"
csv_file_url="https://raw.githubusercontent.com/sefineh-ai/Neo4j/refs/heads/main/data/employee.csv"

cypher_queries = [
    # "CREATE INDEX product_id FOR (product:Product) ON (product.id)",
    # "CREATE INDEX profile_id FOR (profile:Profile) ON (profile.id)",
    # "CREATE INDEX accountant_id FOR (accountant:Accountant) ON (accountant.id)",
    # "CREATE INDEX company_id FOR (company:Company) ON (company.id)",
    "CREATE INDEX employee_id FOR (employee:Employee) ON (employee.id)"
    
]

try:
    for query in cypher_queries:
        result = conn.query(query)
        print(f"Executed: {query}")
        results = conn.query(query)
        print("INDEX CREATED!")
except Exception as e:
    print(f"Error: {e}")
finally:
    conn.close()
