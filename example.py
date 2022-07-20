# pip3 install neo4j-driver
# python3 example.py

from neo4j import GraphDatabase, basic_auth

driver = GraphDatabase.driver(
  "neo4j+s://<DBHASH>.databases.neo4j.io:7687",
  auth=basic_auth("<USERNAME>", "<PASSWORD>"))

# Cypher query
cypher_query = '''
Match (m:Movie) where m.released > 2000 RETURN m limit 5
'''

with driver.session(database="neo4j") as session:
    results = session.run(cypher_query).data()

for record in results:
    print(record['m']['title'])

driver.close()
