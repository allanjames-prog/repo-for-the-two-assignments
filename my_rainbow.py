import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Light blue background to represent the sky

# Create a turtle
pen = turtle.Turtle()
pen.speed(10)  # Fastest drawing speed
pen.width(2)   # Thinner lines for better appearance

# Define the colors of the rainbow
colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]

# Function to draw a filled semi-circle
def draw_filled_semi_circle(radius, color):
    pen.color(color)
    pen.begin_fill()  # Start filling the shape
    pen.penup()
    pen.goto(0, -radius)  # Move to the starting position
    pen.pendown()
    pen.circle(radius, 180)  # Draw a semi-circle
    pen.end_fill()  # End filling the shape

# Draw the rainbow smoothly
radius = 200  # Starting radius
pen.penup()  # Lift the pen initially
pen.goto(0, -radius)  # Move to the starting position
pen.pendown()  # Put the pen down to start drawing

for color in colors:
    pen.color(color)
    pen.begin_fill()  # Start filling the shape
    pen.circle(radius, 180)  # Draw a semi-circle
    pen.end_fill()  # End filling the shape
    radius -= 20  # Decrease the radius for the next arc

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()