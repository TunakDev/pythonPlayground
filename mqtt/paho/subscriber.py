from paho.mqtt import client as mqtt

clientId = "subscriber"
port = 1883
broker = "localhost"


def on_message(client, userdata, message):
    print(f'Payload: {message.payload}')


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, clientId)
client.username_pw_set(username="user1", password="mosquitto")
client.on_message = on_message
client.connect(broker, port)
client.subscribe("Test")
client.loop_forever()

