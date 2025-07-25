import requests
import time
import matplotlib.pyplot as plt

#API endpoint
curr_vals_url = 'http://127.0.0.1:5000/getCurrVal'

def fetch_data():
    #Fetch current data from the Flask API.
    response = requests.get(curr_vals_url)
    if response.status_code == 200:
        return response.json()
    return None


def plot_data(time_vals, measure_vals):
    #Plot the data.
    plt.clf()  # Clear the plot
    plt.plot(time_vals, measure_vals, lw=2)
    plt.xlabel("Time")
    plt.ylabel("Measurement")
    plt.title("Real-time Data Plot")
    plt.draw()
    plt.pause(0.1)


def main():
    plt.ion()  # Turn on interactive mode for Matplotlib
    while True:
        # Fetch current values from the API
        data = fetch_data()
        if data:
            time_vals = data['time']
            measure_vals = data['values']
            plot_data(time_vals, measure_vals)
        else:
            print("Failed to fetch data")

        time.sleep(2)  # Wait for a second before fetching data again

if __name__ == '__main__':
    main()