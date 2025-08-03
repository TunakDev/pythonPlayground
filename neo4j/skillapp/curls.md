## PERSONS

curl -X GET http://127.0.0.1:5050/getPersons

curl -X GET http://127.0.0.1:5050/getPerson?username=jack.tester@testing.com

curl -X POST http://127.0.0.1:5050/createPerson?username=jack.tester@testing.com
curl -X POST http://127.0.0.1:5050/createPerson?username=jack.tester.second@testing.com

curl -X DELETE http://127.0.0.1:5050/deletePerson?username=jack.tester.second@testing.com

## SKILLS

curl -X GET http://127.0.0.1:5050/getSkills

curl -X POST http://127.0.0.1:5050/createSkill?name=Python

Watch the single quotes!
curl -X POST 'http://127.0.0.1:5050/createSkill?name=Java&force=true'

curl -X DELETE http://127.0.0.1:5050/deleteSkill?name=Java3

Watch the single quotes!
curl -X POST 'http://127.0.0.1:5050/hasLearned?username=jack.tester@testing.com&skillname=Java3&level=1'

Watch the single quotes!
curl -X POST 'http://127.0.0.1:5050/changeLevelLearned?username=jack.tester@testing.com&skillname=Java&level=1'

curl -X GET http://127.0.0.1:5050/getSkillsOf?username=jack.tester@testing.com


Upload JSON:
curl --header "Content-Type: application/json" --request POST --data '{"username":"steven.tester@testing.com", "skills":[{"name":"java", "level":"5"},{"name":"python", "level":"4"}]}' http://127.0.0.1:5050/uploadProfile



Delete Duplicated:
MATCH (n:Person)
WITH n.username='jack.tester@testing.com' as userZ, COLLECT(n) as branches
WHERE SIZE(branches) > 1
FOREACH (a IN TAIL(branches) | DETACH DELETE a)

MATCH (n:Skill)
WITH n.name='java' as skillZ, COLLECT(n) as branches
WHERE SIZE(branches) > 1
FOREACH (a IN TAIL(branches) | DETACH DELETE a)

MATCH (n:Person) -[r:Has_Learned]-> (s:Skill) DETACH DELETE n, s


Should work on GitBash:
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"xyz","password":"xyz"}' \
  http://localhost:3000/api/login

For Windows CLI:
curl -H "Content-Type: application/json" -X POST "http://127.0.0.1:5984/test" -d {"""valid""":"""json"""}


Add Swagger (Flasgger) to API:
https://www.youtube.com/watch?v=Oqg83g4khzc