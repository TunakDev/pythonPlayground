from flask import Flask, jsonify
from neo4j import GraphDatabase

URI = "neo4j://localhost"
AUTH = ("neo4j", "neo4jTri4lPa55w0rd")


driver = GraphDatabase.driver(URI, auth=AUTH)
session = driver.session()
app = Flask(__name__)

@app.route('/loadData', methods=['GET'])
def load_data():
    load_modules="""
    LOAD CSV WITH HEADERS FROM 'file:///modules.csv' AS csvLine
    MERGE (module:Module {id: csvLine.id})
    ON CREATE SET module.name = csvLine.name
    MERGE (parentModule:Module {name: coalesce(csvLine.parent_name, csvLine.name)})
    MERGE (parentModule)-[:HAS_MODULE]->(module)
    WITH parentModule, module
    MATCH (selfReferencingModule:Module) -[relation:HAS_MODULE]->(selfReferencingModule)
    DELETE relation
    RETURN parentModule, module
        """

    load_sensors = """
    LOAD CSV WITH HEADERS FROM 'file:///sensors.csv' AS row
    MATCH (module:Module{name:row.parent_name})
    MERGE (s:Sensor{id:row.id,name:row.name})
    MERGE (module) -[:HAS_SENSOR]-> (s)
    RETURN module,s
        """

    load_measurements_smeltery = """
    LOAD CSV WITH HEADERS FROM 'file:///measurementsSmeltery.csv' AS row
    MERGE (s:Sensor{name: row.name})
    MERGE (m:Measurement{timestamp: row.timestamp, currentTempCelsius: toInteger(row.current_temp_celsius)})
    MERGE (s) -[:MEASURED]-> (m)
    RETURN s,m
        """

    load_measurements_crusher = """
    LOAD CSV WITH HEADERS FROM 'file:///measurementsCrusher.csv' AS row
    MERGE (s:Sensor{name: row.name})
    MERGE (m:Measurement{timestamp: row.timestamp, displacement_mm: toInteger(row.displacement_mm),
    velocity_mm_per_second: toInteger(row.velocity_mm_per_second), 
    acceleration_mm_per_second_squared: toInteger(row.acceleration_mm_per_second_squared)})
    MERGE (s) -[:MEASURED]-> (m)
    RETURN s,m
        """

    try:
        print(f'loading modules...')
        session.run(load_modules)
        print(f'modules loaded')
        print(f'loading sensors...')
        session.run(load_sensors)
        print(f'sensors loaded')
        print(f'loading measurements for smeltery...')
        session.run(load_measurements_smeltery)
        print(f'measurements for smeltery loaded')
        print(f'loading measurements for crusher...')
        session.run(load_measurements_crusher)
        print(f'measurements for crusher loaded')
        return f"data successfully loaded"
    except Exception as e:
        return str(e)

@app.route('/getModules', methods=['GET'])
def get_modules():
    q1 = """
        MATCH (n:Module) RETURN n
        """
    results = session.run(q1)
    data=results.data()
    return jsonify(data)

@app.route('/getSensors', methods=['GET'])
def get_sensors():
    q1 = """
            MATCH (n:Sensor) RETURN n
            """
    results = session.run(q1)
    data = results.data()
    return jsonify(data)

@app.route('/getMeasurements', methods=['GET'])
def get_measurements():
    q1 = """
            MATCH (n:Measurement) RETURN n
            """
    results = session.run(q1)
    data = results.data()
    return jsonify(data)

@app.route('/getAll', methods=['GET'])
def get_all():
    q1 = """
            MATCH (n) RETURN n
            """
    results = session.run(q1)
    data = results.data()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5050)