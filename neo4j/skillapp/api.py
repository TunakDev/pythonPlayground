from flask import Flask, jsonify, request, render_template_string
from neo4j import GraphDatabase, Query

URI = "neo4j://localhost"
AUTH = ("neo4j", "neo4jTri4lPa55w0rd")

driver = GraphDatabase.driver(URI, auth=AUTH)
session = driver.session()
app = Flask(__name__)


@app.route('/getPersons', methods=['GET'])
def get_persons():
    match_query = Query("MATCH (n:Person) RETURN n")
    results = session.run(match_query)
    data = results.data()
    return jsonify(data)


# use parameters like [...]/getPerson?username=jack.tester@testing.com
@app.route('/getPerson', methods=['GET'])
def get_person():
    username = request.args.get("username")
    if username is None:
        return render_template_string("No username provided. Use '/getPerson?username=<username>' instead"), 400
    match_query = Query("MATCH (n:Person {username: $username}) RETURN n")
    results = session.run(match_query, username=username)
    data = results.data()
    if not data:
        return render_template_string("The user '{{username}}' was not found. Consider creating it first", username=username), 404
    return jsonify(data)


# use parameters like [...]/createPerson?username=jack.tester@testing.com
@app.route('/createPerson', methods=['POST'])
def create_person():
    username = request.args.get("username")
    if username is None:
        return render_template_string("No username provided. Use '/createPerson?username=<username>' instead"), 400
    match_query = Query("MATCH (n:Person {username: $username}) RETURN n")
    results = session.run(match_query, username=username)
    data = results.data()
    # when user is created there is no "data"
    if not data:
        create_query = Query("CREATE (n:Person {username: $username}) RETURN n")
        results = session.run(create_query, username=username)
        data = results.data()
    else:
        return render_template_string("The user '{{username}}' already exists.", username=username), 409
    return jsonify(data)


# use parameters like [...]/deletePerson?username=jack.tester@testing.com
@app.route('/deletePerson', methods=['DELETE'])
def delete_person():
    username = request.args.get("username")
    if username is None:
        return render_template_string("No username provided. Use '/deletePerson?username=<username>' instead"), 400
    match_query = Query("MATCH (n:Person {username: $username}) RETURN n")
    results = session.run(match_query, username=username)
    data = results.data()
    if not data:
        return render_template_string("The user '{{username}}' was not found.", username=username), 404
    else:
        match_delete_query = Query("MATCH (n:Person {username: $username}) DETACH DELETE n")
        session.run(match_delete_query, username=username)
        return render_template_string("The user '{{username}}' was successfully deleted.", username=username), 200


@app.route('/getSkills', methods=['GET'])
def get_skills():
    match_query = Query("MATCH (n:Skill) RETURN n")
    results = session.run(match_query)
    data = results.data()
    return jsonify(data)


# use parameters like [...]/createSkill?name=Java or '[...]/createSkill?name=<skillname>&force=true' with single quotes
@app.route('/createSkill', methods=['POST'])
def create_skill():
    skillname = request.args.get("name")
    force = request.args.get("force")
    create_query = Query("CREATE (n:Skill {name: toLower($skillname)}) RETURN n")
    if skillname is None:
        return render_template_string("No skillname provided. Use '/createSkill?name=<skillname>' instead"), 400
    if force == "true":
        print("FORCED CREATION OF A SKILL")
        results = session.run(create_query, skillname=skillname)
        return jsonify(results.data())
    match_query = Query("MATCH (n:Skill) WHERE n.name=~ '.*' + toLower($skillname) + '.*' RETURN n")
    results = session.run(match_query, skillname=skillname)
    data = results.data()
    if not data:
        results = session.run(create_query, skillname=skillname)
        return jsonify(results.data())
    else:
        warning_message = "These skills are already in the database. Does the one you wanted to add already exist?"
        warning_message2 = "If you want to add your skill use the force parameter like '/createSkill?name=<skillname>&force=true'"
        warning_message3 = "When you do this with curl you have to add single quotes around the url!"
        return jsonify({
            "warning": warning_message,
            "warning2": warning_message2,
            "warning3": warning_message3,
            "skills":data
        })


# use parameters like [...]/deleteSkill?name=Java
@app.route('/deleteSkill', methods=['DELETE'])
def delete_skill():
    skillname = request.args.get("name")
    if skillname is None:
        return render_template_string("No skillname provided. Use '/delete_skill?name=<skillname>' instead"), 400
    match_query = Query("MATCH (n:Skill {name: toLower($skillname)}) RETURN n")
    results = session.run(match_query, skillname=skillname)
    data = results.data()
    if not data:
        return render_template_string("The skill '{{skillname}}' was not found.", skillname=skillname), 404
    else:
        match_delete_query = Query("MATCH (n:Skill {name: toLower($skillname)}) DETACH DELETE n")
        session.run(match_delete_query, skillname=skillname)
        return render_template_string("The skill '{{skillname}}' was successfully deleted.", skillname=skillname), 200


# use parameters like '[...]/hasLearned?username=jack.tester@testing.com&skillname=Java&level=3' with single quotes
@app.route('/hasLearned', methods=['POST'])
def has_learned():
    username = request.args.get("username")
    skillname = request.args.get("skillname")
    skilllevel = request.args.get("level")
    if username is None:
        return render_template_string("No username provided. Use '[...]/hasLearned?username=<username>&skillname=<skillname>&level=<skilllevel>' with single quotes instead"), 400
    if skillname is None:
        return render_template_string("No skillname provided. Use '[...]/hasLearned?username=<username>&skillname=<skillname>&level=<skilllevel>' with single quotes instead"), 400
    if skilllevel is None:
        return render_template_string("No skilllevel provided. Use '[...]/hasLearned?username=<username>&skillname=<skillname>&level=<skilllevel>' with single quotes instead"), 400
    match_query = Query("MATCH (u:Person {username:$username}) -[r:Has_Learned]-> (s:Skill {name:toLower($skillname)}) RETURN r")
    results = session.run(match_query, username=username, skilllevel=skilllevel, skillname=skillname)
    data = results.data()
    if not data:
        create_query = Query(
            "MATCH (n:Person{username:$username}) MATCH (s:Skill{name:$skillname}) MERGE (n) -[r:Has_Learned{level:$skilllevel}]-> (s)")
        results = session.run(create_query, username=username, skillname=skillname, skilllevel=skilllevel)
        return jsonify(results.data())
    else:
        return render_template_string("This person has already learned that skill on the same or another level. If you wish to change the level of the skill use '[...]/changeLevelLearned?username=<username>&skillname=<skillname>&level=<skilllevel>' with single quotes"), 409


# use parameters like '[...]/changeLevelLearned?username=jack.tester@testing.com&skillname=Java&level=3' with single quotes
@app.route('/changeLevelLearned', methods=['POST'])
def change_level_learned():
    username = request.args.get("username")
    skillname = request.args.get("skillname")
    skilllevel = request.args.get("level")
    if username is None:
        return render_template_string(
            "No username provided. Use '[...]/hasLearned?username=<username>&skillname=<skillname>&level=<skilllevel>' with single quotes instead"), 400
    if skillname is None:
        return render_template_string(
            "No skillname provided. Use '[...]/hasLearned?username=<username>&skillname=<skillname>&level=<skilllevel>' with single quotes instead"), 400
    if skilllevel is None:
        return render_template_string(
            "No skilllevel provided. Use '[...]/hasLearned?username=<username>&skillname=<skillname>&level=<skilllevel>' with single quotes instead"), 400
    update_query = Query("MATCH (u:Person) -[r:Has_Learned]-> (s:Skill) WHERE u.username=$username AND s.name=$skillname SET r.level=$skilllevel")
    session.run(update_query, username=username, skillname=skillname, skilllevel=skilllevel)
    return render_template_string("The level of the skill was successfully changed"), 200


# use parameters like [...]/getSkillsOf?username=jack.tester@testing.com
@app.route('/getSkillsOf', methods=['GET'])
def get_skills_of():
    username = request.args.get("username")
    if username is None:
        return render_template_string(
            "No username provided. Use [...]/getSkillsOf?username=<username> instead"), 400
    match_query = Query("MATCH (n:Person{username:$username}) -[r:Has_Learned]-> (s:Skill) RETURN r.level, s")
    results = session.run(match_query, username=username)
    return jsonify(results.data())


# use curl like curl --header "Content-Type: application/json" --request POST --data '{"username":"steven.tester@testing.com", "skills":[{"name":"java", "level":"5"},{"name":"python", "level":"4"}]}' http://127.0.0.1:5050/uploadProfile
@app.route('/uploadProfile', methods=['POST'])
def upload_profile():
    username = request.json['username']
    skills = request.json['skills']
    if username is None:
        return render_template_string(
            "No username provided. Add a username like \"username\":\"steven.tester@testing.com\""), 400
    if skills is None:
        return render_template_string(
            "No skills provided. Add skills like \"skills\":[{\"name\":\"java\", \"level\":\"5\"},{\"name\":\"python\", \"level\":\"4\"}]"), 400

    #CREATING USER IF IT DOES NOT EXIST
    match_query = Query("MATCH (n:Person {username: $username}) RETURN n")
    results = session.run(match_query, username=username)
    data = results.data()
    # when user is not yet created there is no "data"
    if not data:
        create_query = Query("CREATE (n:Person {username: $username}) RETURN n")
        results = session.run(create_query, username=username)
        data = results.data
        if data:
            print(f"user {username} successfully created")
        else:
            print(f"user {username} was not created due to a failure while passing the creation-query")
    else:
        print(f"user {username} already exsists - continue")

    for skill in skills:
        skillname = skill['name']
        # CREATING SKILL IF IT DOES NOT EXIST
        match_query = Query("MATCH (n:Skill {name: $skillname}) RETURN n")
        results = session.run(match_query, skillname=skillname)
        data = results.data()
        # when skill is not yet created there is no "data"
        if not data:
            create_query = Query("CREATE (n:Skill {name: $skillname}) RETURN n")
            results = session.run(create_query, skillname=skillname)
            data = results.data
            if data:
                print(f"skill {skillname} successfully created")
            else:
                print(f"skill {skillname} was not created due to a failure while passing the creation-query")
        else:
            print(f"skill {skillname} already exsists - continue")

        #LINK SKILL TO PERSON
        skilllevel = skill['level']
        match_query = Query("MATCH (n:Person{username: $username})-[r:Has_Learned]->(s:Skill{name: $skillname}) RETURN r")
        results = session.run(match_query, username=username, skillname=skillname)
        data = results.data()
        # when skill is not yet created there is no "data"
        if not data:
            create_query = Query("MATCH (n:Person{username:$username}) MATCH (s:Skill{name:$skillname}) MERGE (n) -[r:Has_Learned{level:$skilllevel}]-> (s)")
            results = session.run(create_query, username=username, skilllevel=skilllevel, skillname=skillname)
            data = results.data
            if data:
                print(f"person {username} successfully learned skill {skillname}")
            else:
                print(f"person {username} can not learn skill {skillname} due to a failure while passing the creation-query")
        else:
            print(f"person {username} is already proficient in skill {skillname} on the same or another level. If you want to change the level consider using: '[...]/changeLevelLearned?username=<username>&skillname=<skillname>&level=<skilllevel>' with single quotes")

    return "Process terminated successfully. Check logs for possibly occurred errors"

#todo realize json upload for whole profiles
#todo Projects
#todo Map Projects to Skills
#todo get persons with skills by graph (project -> skill -has_learned(level:X)-> person)

if __name__ == '__main__':
    app.run(debug=True, port=5050)
