import pandas as pd # type: ignore
import numpy as np  # type: ignore
directory_path = 'data/nodes/connection.csv'
df = pd.read_csv(directory_path)
sender_profile_id = df['sender_profile_id']
receiver_profile_id = df['receiver_profile_id']
connection_id = df['id']
df_srel = pd.DataFrame({"start_id":connection_id, "end_id":sender_profile_id, "type":"SENDER"})
df_rrel = pd.DataFrame({"start_id":connection_id, "end_id":receiver_profile_id, "type":"RECEIVER"})
df_srel.to_csv("data/relations/connection__sender_profile.csv", index=False)
df_rrel.to_csv("data/relations/connection__receiver_profile.csv", index=False)
'''
LOAD CSV WITH HEADERS FROM "file:///data/nodes/connection.csv" as row
WITH keys(row) AS headers, row
UNWIND headers AS header
MERGE (entity:DataNode{id: row.id, type_con:"connection"})
SET entity[header] = coalesce(row[header], 'null')
RETURN entity


LOAD CSV WITH HEADERS FROM "file:///data/relations/connection__sender_profile.csv" as row
WITH row
MATCH(connection:DataNode{id:row.start_id, type_con:"connection"})
MATCH (profile:DataNode{id:row.end_id, type:"profile"})
MERGE (connection)-[r:SENDER]->(profile)
RETURN connection, r, profile


LOAD CSV WITH HEADERS FROM "file:///data/relations/connection__receiver_profile.csv" as row
WITH row
MATCH(connection:DataNode{id:row.start_id, type_con:"connection"})
MATCH (profile:DataNode{id:row.end_id, type:"profile"})
MERGE (connection)-[r:RECEIVER]->(profile)
RETURN connection, r, profile

'''