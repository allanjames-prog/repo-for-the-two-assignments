import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
pen = turtle.Turtle()
pen.speed(10)
pen.color("pink")
pen.fillcolor("pink")  # Set fill color to pink
pen.width(2)

# Function to draw a full heart
def draw_heart(size):
    pen.begin_fill()
    pen.left(50)
    pen.forward(size)
    pen.circle(size * 0.6, 200)  # Adjusted for a better heart shape
    pen.left(140)
    pen.circle(size * 0.6, 200)  # Adjusted for a better heart shape
    pen.forward(size)
    pen.end_fill()
    pen.setheading(0)

# Draw the main heart
pen.penup()
pen.goto(0, -100)
pen.pendown()
draw_heart(150)

# Function to draw sub-hearts
def draw_sub_heart(x, y, size):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    draw_heart(size)

# Draw sub-hearts inside the main heart
draw_sub_heart(-50, 50, 30)
draw_sub_heart(50, 50, 30)
draw_sub_heart(0, 0, 30)

# Hide the turtle and display the result
pen.hideturtle()
turtle.done()