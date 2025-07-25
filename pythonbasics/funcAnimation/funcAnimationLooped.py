import matplotlib.pyplot as plt
import numpy as np
import time

# Create a figure and axis
fig, ax = plt.subplots()

# Set the axis limits, but will adjust dynamically later
ax.set_ylim(0, 10)  # y-axis range

# Create an empty line object
line, = ax.plot([], [], lw=2)

# Create empty lists to store x and y values
x_vals = []
y_vals = []

# Define the maximum number of values to show
max_points = 20

# Define a function to update the plot
def update_plot(i):
    # Add a new point to the data
    x_vals.append(i)
    y_vals.append(np.random.randint(0, 10))  # You can add any logic for generating y-values

    # If the data exceeds the max points, remove the oldest value
    if len(x_vals) > max_points:
        x_vals.pop(0)  # Remove the oldest x value
        y_vals.pop(0)  # Remove the oldest y value

    # Update the data for the line plot
    line.set_data(x_vals, y_vals)

    # Adjust x-axis limits to always show the last 'max_points' values
    ax.set_xlim(x_vals[0], x_vals[-1])  # Set x-axis to show the range of the last max_points

    return line,


# Function to simulate the while loop
def run_dynamic_plot():
    i = 0
    while True:
        update_plot(i)
        plt.draw()  # Redraw the plot
        plt.pause(0.5)  # Pause for 0.2 seconds (simulates the loop running every second)
        i += 1
        if i > 100:  # Stop the loop after 100 points (for this example)
            break


# Display the plot and start the dynamic update
plt.ion()  # Turn on interactive mode
run_dynamic_plot()
plt.ioff()  # Turn off interactive mode after the loop is done
plt.show()
