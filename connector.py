from neo4j import GraphDatabase
class Neo4jConnection:

    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def query(self, query, parameters=None):
        with self._driver.session() as session:
            return session.run(query, parameters)

uri = "neo4j+s://f17af8cb.databases.neo4j.io"  
username = "neo4j"             
password = "iiaAxmgCL4Hbl_tU1fr5lhtzDAI5n5-i8T0PWnyS6-M"    

conn = Neo4jConnection(uri, username, password)
csv_file_path ="data/accountant.csv" 
query = f"""
LOAD CSV WITH HEADERS FROM {csv_file_path} AS row
"""
result = conn.query(query)

