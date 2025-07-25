import serial
import signal
import re
from datetime import datetime

def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def format_sensor_string(string):
    formatted_string = string[2:-5]
    formatted_string = formatted_string.replace('\\xc2\\xb0', '')
    return formatted_string + "\n"


def extract_number_data_from_string(string):
    return (datetime.now().strftime("%Y-%m-%d-%H:%M:%S") +
            ", " +
            str([float(s) for s in re.findall(r'\d+.\d+', string)])[1:-1] +
            ", 0" +
            "\n")


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)
interrupted = False

if __name__ == '__main__':
    ser = serial.Serial('COM6')
    with open("testdata.csv", 'w') as f:
        # write headers on file initially
        f.write("Timestamp,Humidity,Temperature Celsius,Temperature Fahrenheit, Heat Index Celsius,Heat Index Fahrenheit, Anomaly\n")
        while True:
            if ser.in_waiting > 0:
                temp = ser.readline()
                string_to_write = format_sensor_string(str(temp))
                print(string_to_write)
                extracted_values_from_sensor_reading = extract_number_data_from_string(string_to_write)
                print(extracted_values_from_sensor_reading)
                if extracted_values_from_sensor_reading.count(',') == 6:
                    # do not write faulty data produced by a late read from serial
                    f.write(extracted_values_from_sensor_reading)

            if interrupted:
                break
