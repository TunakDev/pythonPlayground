from neo4j import GraphDatabase

URI = "neo4j://localhost"
AUTH = ("neo4j", "neo4jTri4lPa55w0rd")

with GraphDatabase.driver(URI, auth=AUTH) as driver:
    driver.verify_connectivity()

records, summary, keys = driver.execute_query(
    "MATCH (s:Sensor) -[:MEASURED]-> (m:Measurement) RETURN s,m"
)

for entry in records:
    print(entry)

print("The Query `{query}` returned {records_count} records in {time} ms.".format(
    query=summary.query, records_count=len(records), time=summary.result_available_after
))






# Delete all nodes and relations
# MATCH (n)
# DETACH DELETE n