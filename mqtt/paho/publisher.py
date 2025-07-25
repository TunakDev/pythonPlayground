from paho.mqtt import client as mqtt
import time

clientId = "publisher"
port = 1883
broker = "localhost"


client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, clientId)
client.username_pw_set(username="user1", password="mosquitto")
client.connect(broker, port)
client.loop_start()


topic = "Test"
msg_count = 0

try:
    while msg_count < 10:
        time.sleep(1)
        msg_count += 1
        result = client.publish(topic, msg_count)
        status = result[0]
        if status == 0:
            print("Message "+ str(msg_count) + " is published to topic " + topic)
        else:
            print("Failed to send message to topic " + topic)
            if not client.is_connected():
                print("Client not connected, exiting...")
                break
finally:
    client.disconnect()
    client.loop_stop()