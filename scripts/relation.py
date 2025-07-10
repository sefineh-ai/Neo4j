# from neo4j import GraphDatabase # type: ignore
# from dotenv import load_dotenv # type: ignore
# import os

# load_dotenv()
# class Neo4jConnection:

#     def __init__(self, uri, user, password):
#         self._driver = GraphDatabase.driver(uri, auth=(user, password))

#     def close(self):
#         self._driver.close()

#     def query(self, query, parameters=None):
#         with self._driver.session() as session:
#             result = session.run(query, parameters)
#             data = [record.data() for record in result]
#             return data

# uri = os.getenv("NEO4J_URI") 
# username = os.getenv("NEO4J_USERNAME")             
# password = os.getenv("NEO4J_PASSWORD")    

# conn = Neo4jConnection(uri, username, password)
# csv_file_url = "https://raw.githubusercontent.com/sefineh-ai/Neo4j/main/data/accountant.csv"

# RELATION="ACCOUNTANT__TO__PROFILE"
# RELATION_VALUE=os.getenv(RELATION)
# relation_name, ids = RELATION_VALUE.split("@")
# left_id = ids.split(",")[0][1:]
# right_id = ids.split(",")[1][:-1]
# label_names =  RELATION.split("__")
# left_label_name = label_names[0].capitalize()
# right_label_name = label_names[-1].capitalize()


# cypher_query = f"""
#     LOAD CSV WITH HEADERS FROM '{csv_file_url}' AS row
#     MATCH ({left_label_name.lower()}:{left_label_name} {{id: row.{left_id}}})
#     MATCH ({right_label_name.lower()}:{right_label_name} {{id: row.{right_id}}})
#     MERGE ({left_label_name.lower()})-[:{relation_name}]->({right_label_name.lower()})
#     """
# try:
#     result = conn.query(cypher_query)
#     print(f"Executed: {cypher_query}")    
# except Exception as e:
#     print(f"Error: {e}")
# finally:
#     conn.close()
import pandas as pd 
import numpy as np 
import os 
# id,clave,comment,created_at,currency_code,currency_exchange_rate,hacienda_responsexmlpath,
# issue_date,medio_pago_details,original_notaxmlpath,pdf_path,price_with_tax,price_without_tax,
# receiver_email,receiver_identification,receiver_name,sender_email,sender_name,
# sender_tax_payer_id,status,tax,total_comprobante,total_descuentos,total_exento,total_gravado,
# total_impuesto,total_mercancias_exentas,total_serv_gravados,total_venta,total_venta_neta,type,
# codigo_actividad_id,condicion_venta_id,facturas_id,medio_pago_id,sender_profile_id
df = pd.read_csv("data/nodes/subscription_plan.csv",
                 on_bad_lines="skip"
                 )
df[['id', "currency_id"]].to_csv("data/relations/subscription_plan__currency.csv", index=False)


