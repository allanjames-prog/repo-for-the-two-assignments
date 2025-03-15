import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("bisque")

# Create a turtle object
pen = turtle.Turtle()
pen.shape("turtle")
pen.speed(10)  # Fastest speed

# Function to draw a petal
def draw_petal(radius, angle):
    pen.circle(radius, angle)
    pen.left(180 - angle)
    pen.circle(radius, angle)
    pen.left(180 - angle)

# Function to draw a layer of petals
def draw_layer(num_petals, petal_radius, petal_angle, color):
    pen.color(color)
    for _ in range(num_petals):
        draw_petal(petal_radius, petal_angle)
        pen.left(360 / num_petals)

# Function to draw the flower
def draw_flower():
    # Draw outer layer
    draw_layer(12, 150, 60, "pink")
    # Draw middle layer
    draw_layer(8, 100, 45, "lightblue")
    # Draw inner layer
    draw_layer(6, 50, 30, "yellow")

    # Draw the center of the flower
    pen.color("orange")
    pen.penup()
    pen.goto(0, -20)  # Move to the center
    pen.pendown()
    pen.begin_fill()
    pen.circle(20)  # Draw a circle for the center
    pen.end_fill()

# Draw the flower
draw_flower()

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()