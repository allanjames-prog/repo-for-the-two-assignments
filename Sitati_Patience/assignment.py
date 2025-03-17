import turtle
import math

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("skyblue")  # Background color

# Create turtle object
tr = turtle.Turtle()
tr.speed(7)  # Moderate speed

# Function to draw a rectangle (for tree trunk)
def draw_rectangle(color, x, y, width, height):
    tr.penup()
    tr.goto(x, y)
    tr.pendown()
    tr.color(color)
    tr.begin_fill()
    
    for _ in range(2):
        tr.forward(width)
        tr.left(90)
        tr.forward(height)
        tr.left(90)
    
    tr.end_fill()

# Function to draw a circle (for leaves, flowers, and sun)
def draw_circle(color, x, y, radius):
    tr.penup()
    tr.goto(x, y - radius)  # Adjust to center the circle
    tr.pendown()
    tr.color(color)
    tr.begin_fill()
    tr.circle(radius)
    tr.end_fill()

# Function to draw a tree at a given position
def draw_tree(x, y):
    draw_rectangle("brown", x, y, 20, 60)  # Tree trunk
    draw_circle("darkgreen", x + 10, y + 60, 30)  # Leaves

# Function to draw the rainbow
def draw_rainbow():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    radius = 200
    x, y = -radius, -50  # Adjusting start position of the rainbow
    
    for color in colors:
        tr.penup()
        tr.goto(x, y)
        tr.pendown()
        tr.color(color)
        tr.width(20)
        tr.setheading(60)  # Adjust arc angle
        tr.circle(radius, 120)  # Draw an arc
        radius -= 10  # Reduce radius for the next arc

# Function to draw a flower
def draw_flower(x, y):
    petal_color = "pink"
    center_color = "yellow"
    
    for _ in range(5):  # Draw 5 petals
        draw_circle(petal_color, x, y, 10)
        tr.right(72)  # Rotate for the next petal
    
    draw_circle(center_color, x, y, 5)  # Flower center

# Draw the ground (grass)
draw_rectangle("green", -400, -100, 800, 200)

# Draw the trees
tree_positions = [-250, -150, -50, 50, 150, 250]
for pos in tree_positions:
    draw_tree(pos, -50)

# Draw the rainbow
draw_rainbow()

# Draw flowers in the forest
flower_positions = [(-200, -60), (-100, -70), (0, -65), (100, -75), (200, -60)]
for x, y in flower_positions:
    draw_flower(x, y)

# Hide the turtle
tr.hideturtle()

# Keep the window open
turtle.done()
