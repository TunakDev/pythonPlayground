Guide: https://www.youtube.com/watch?v=XGrHsDl5Ewc

>>> Broker on Docker-Container has to run for this code to work! use docker-compose in folder /mosquitto/.

Mosquitto Broker:
https://github.com/sukesh-ak/setup-mosquitto-with-docker -> create pwfile
https://cedalo.com/blog/mosquitto-docker-configuration-ultimate-guide/#How_to_install_and_configure_Mosquitto_MQTT_broker_in_Docker_from_scratch

On error "Client myClient disconnected, not authorised." -> restart container


To run container:
- map volume for pwfile
- run docker-compose up
- connect to docker container (open terminal inside docker container)
- use commands to create user and pw (note them!)
- use user and pw later on in the connection inside the code


Guide (write own broker) https://www.youtube.com/watch?v=Q5cxPTKN5nE