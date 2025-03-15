
import turtle
tr = turtle.Turtle()

# Create a new turtle screen and set its background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a new turtle object
rainbow = turtle.Turtle()
rainbow.speed(0)  # Fastest speed

# Define the colors of the rainbow
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Draw the rainbow
for i in range(180):
    rainbow.pencolor(colors[i % 7])  # Cycle through the colors
    rainbow.forward(2)  # Move forward by 2 units
    rainbow.left(2)  # Turn left by 2 degrees

# Keep the window open
turtle.done()
