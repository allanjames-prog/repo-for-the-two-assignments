import turtle

def draw_petal():
    turtle.circle(100, 60)  # Draw a semicircle
    turtle.left(120)        # Turn left
    turtle.circle(100, 60)  # Draw another semicircle
    turtle.left(120)        # Turn left to the original position

def draw_flower():
    turtle.color("red")     # Set the color of the petals
    turtle.begin_fill()     # Start filling the color
    for _ in range(6):      # Draw 6 petals
        draw_petal()
        turtle.left(60)      # Turn to position for the next petal
    turtle.end_fill()       # End filling the color

def draw_stem():
    turtle.right(90)        # Turn to face downwards
    turtle.color("green")   # Set the color of the stem
    turtle.pensize(10)      # Set the thickness of the stem
    turtle.forward(200)      # Draw the stem

# Set up the turtle
turtle.speed(10)            # Set the speed of drawing
turtle.bgcolor("lightblue") # Set the background color

# Draw the flower and stem
draw_flower()
draw_stem()

# Finish up
turtle.hideturtle()         # Hide the turtle
turtle.done()               # Finish the drawing