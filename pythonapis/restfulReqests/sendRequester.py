import requests
import time
import json
import random

# API endpoint
control_url = 'http://127.0.0.1:5000/loop-status'
post_url = 'http://127.0.0.1:5000/sender'

# Function to check if the loop is allowed to run
def is_loop_running():
    response = requests.get(control_url)
    if response.status_code == 200:
        return True
    return False

def send_post_request():
    data = {
        "name": "RandTempSensor",
        "unit": "degrees C",
        "value": round(random.uniform(10.0, 25.5),2)
    }
    response = requests.post(post_url, json=data)
    if response.status_code == 201:
        print(f"Successfully sent measurement: Sensor {data['name']} sent {data['value']} {data['unit']}")
    else:
        print(f"Failed to send measurement. Status code: {response.status_code}, Message: {response.text}")


while True:
    if is_loop_running():
        send_post_request()
        time.sleep(2)  # Wait for 2 seconds before sending another request
    else:
        print("Loop is not running. Waiting for start.")
        time.sleep(2)  # Check every 2 seconds if the loop should start