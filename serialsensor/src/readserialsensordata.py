import serial
ser = serial.Serial('COM6', 9600, timeout=None)


def format_sensor_string(string):
    formatted_string = string[2:-5]
    formatted_string = formatted_string.replace('\\xc2\\xb0', '°')
    return formatted_string


while True:
    data = ser.readline()

    #print(str(data))
    print(format_sensor_string(str(data)))