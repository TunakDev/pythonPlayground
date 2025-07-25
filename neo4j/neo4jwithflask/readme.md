the corresponding csv for the file upload is located in neo4j/graphdatabase/dockerimports so it can be loaded as a 
volume inside the docker container

>>> First one has to start the Docker-container in neo4j/graphdatabase

Cypher for loading data from csv:


# Load all modules and connect the modules hierarchically
LOAD CSV WITH HEADERS FROM 'file:///modules.csv' AS csvLine
MERGE (module:Module {id: csvLine.id})
ON CREATE SET module.name = csvLine.name
MERGE (parentModule:Module {name: coalesce(csvLine.parent_name, csvLine.name)})
MERGE (parentModule)-[:HAS_MODULE]->(module)
WITH parentModule, module
MATCH (selfReferencingModule:Module) -[relation:HAS_MODULE]->(selfReferencingModule)
DELETE relation
RETURN parentModule, module

# Load all sensors and relate them to the corresponding modules
LOAD CSV WITH HEADERS FROM 'file:///sensors.csv' AS row
MATCH (module:Module{name:row.parent_name})
MERGE (s:Sensor{id:row.id,name:row.name})
MERGE (module) -[:HAS_SENSOR]-> (s)
RETURN module,s

# Load all the measurements from the smeltery and relate them to the corresponding sensors
LOAD CSV WITH HEADERS FROM 'file:///measurementsSmeltery.csv' AS row
MERGE (s:Sensor{name: row.name})
MERGE (m:Measurement{timestamp: row.timestamp, currentTempCelsius: toInteger(row.current_temp_celsius)})
MERGE (s) -[:MEASURED]-> (m)
RETURN s,m

# Load all the measurements from the crusher and relate them to the corresponding sensors
LOAD CSV WITH HEADERS FROM 'file:///measurementsCrusher.csv' AS row
MERGE (s:Sensor{name: row.name})
MERGE (m:Measurement{timestamp: row.timestamp, displacement_mm: toInteger(row.displacement_mm),
velocity_mm_per_second: toInteger(row.velocity_mm_per_second), 
acceleration_mm_per_second_squared: toInteger(row.acceleration_mm_per_second_squared)})
MERGE (s) -[:MEASURED]-> (m)
RETURN s,m
