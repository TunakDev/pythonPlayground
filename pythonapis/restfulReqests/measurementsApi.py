from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import threading

app = Flask(__name__)
CORS(app)

# Global variable to control the POST loop
loop_running = False

# Lock to avoid race conditions
loop_lock = threading.Lock()

time_vals = []
measures_vals = []

time_ctr = 0

@app.route('/sender', methods=['POST'])
def receive_measurement():
    data = request.get_json()
    measures_vals.append(data.get("value"))

    global time_ctr
    time_ctr+=2
    time_vals.append(time_ctr)

    if len(measures_vals) > 20:
        measures_vals.pop(0)
        time_vals.pop(0)

    print(f'Name: {data.get("name")}')
    print(f'Unit: {data.get("unit")}')
    print(f'Value: {data.get("value")}')
    print(f'currently stored values: {measures_vals}')
    print(f'currently stored times: {time_vals}')

    return "Measurement received", 201


@app.route('/getCurrVal', methods=['GET'])
def get_current_values():
    return jsonify({"time": time_vals, "values": measures_vals})


# Route to start the loop
@app.route('/start-loop', methods=['GET'])
def start_loop():
    global loop_running
    with loop_lock:
        if not loop_running:
            loop_running = True
            return jsonify({"message": "Loop started"}), 200
        return jsonify({"message": "Loop is already running"}), 400

# Route to stop the loop
@app.route('/stop-loop', methods=['GET'])
def stop_loop():
    global loop_running
    with loop_lock:
        if loop_running:
            loop_running = False
            return jsonify({"message": "Loop stopped"}), 200
        return jsonify({"message": "Loop is not running"}), 400

@app.route('/loop-status', methods=['GET'])
def get_loop_status():
    if loop_running:
        return "Loop running", 200
    else:
        return "Loop not running", 400


if __name__ == '__main__':
    app.run(debug=True)