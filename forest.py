import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Light blue sky background

# Create a turtle object for drawing
pen = turtle.Turtle()
pen.speed(0)  # Fastest speed
pen.hideturtle()  # Hide the turtle initially

# Function to draw a tree
def draw_tree(x, y, trunk_height, trunk_width, leaf_radius):
    # Draw the trunk
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.color("brown")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(trunk_width)
        pen.left(90)
        pen.forward(trunk_height)
        pen.left(90)
    pen.end_fill()

    # Draw the leaves
    pen.penup()
    pen.goto(x + trunk_width / 2, y + trunk_height)  # Move to the top of the trunk
    pen.pendown()
    pen.color("green")
    pen.begin_fill()
    pen.circle(leaf_radius)
    pen.end_fill()

# Function to draw grass
def draw_grass():
    pen.penup()
    pen.goto(-400, -200)  # Start at the bottom-left corner
    pen.pendown()
    pen.color("green")
    pen.begin_fill()
    for _ in range(2):
        pen.forward(800)  # Draw a rectangle for the grass
        pen.right(90)
        pen.forward(200)
        pen.right(90)
    pen.end_fill()

# Function to draw the sun
def draw_sun():
    pen.penup()
    pen.goto(300, 200)  # Position the sun in the top-right corner
    pen.pendown()
    pen.color("yellow")
    pen.begin_fill()
    pen.circle(50)  # Draw the sun
    pen.end_fill()

# Function to draw clouds
def draw_cloud(x, y):
    cloud = turtle.Turtle()
    cloud.shape("circle")
    cloud.color("white")
    cloud.penup()
    cloud.goto(x, y)
    cloud.pendown()
    cloud.begin_fill()
    for _ in range(4):
        cloud.circle(30, 180)  # Draw a fluffy cloud
        cloud.right(90)
    cloud.end_fill()
    cloud.hideturtle()

# Function to draw a bird
def draw_bird(x, y):
    bird = turtle.Turtle()
    bird.shape("triangle")
    bird.color("black")
    bird.penup()
    bird.goto(x, y)
    bird.pendown()
    bird.setheading(-45)  # Draw the first wing
    bird.forward(20)
    bird.backward(20)
    bird.setheading(45)  # Draw the second wing
    bird.forward(20)
    bird.backward(20)
    bird.hideturtle()

# Draw the forest scene
draw_grass()  # Draw the grass
draw_sun()  # Draw the sun
draw_cloud(-200, 150)  # Draw a cloud on the left
draw_cloud(200, 180)  # Draw a cloud on the right

# Draw multiple trees
for _ in range(5):
    x = random.randint(-300, 300)  # Random x position
    y = random.randint(-200, 0)  # Random y position
    trunk_height = random.randint(50, 150)  # Random trunk height
    trunk_width = random.randint(10, 20)  # Random trunk width
    leaf_radius = random.randint(30, 60)  # Random leaf radius
    draw_tree(x, y, trunk_height, trunk_width, leaf_radius)

# Draw some birds
for _ in range(3):
    x = random.randint(-300, 300)  # Random x position
    y = random.randint(100, 200)  # Random y position
    draw_bird(x, y)

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()