import turtle
import colorsys

def draw_one_colour_arc(x, y, r, pensize, color):
    turtle.up()
    turtle.goto(x + r, y)
    turtle.down()
    turtle.seth(90)
    turtle.pensize(pensize)
    turtle.color(color)
    turtle.circle(r, 270)

# Set up the turtle environment
turtle.speed(0)
turtle.bgcolor('lightblue')
turtle.title('Rainbow Pattern')
turtle.setup(700, 700)
turtle.colormode(1.0)  # Set color mode to 1.0 for float RGB values

num_colors = 49
radius = 300
penwidth = 20 * 7 / num_colors
hue = 0

for i in range(num_colors):
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1, 1)
    draw_one_colour_arc(0, -100, radius, penwidth, (r, g, b))
    radius -= (penwidth - 1)
    hue += 0.9 / num_colors

turtle.done()
import turtle
import colorsys

def draw_one_colour_arc(x, y, r, pensize, color):
    turtle.up()
    turtle.goto(x + r, y)
    turtle.down()
    turtle.seth(90)
    turtle.pensize(pensize)
    turtle.color(color)
    turtle.circle(r, 270)

# Set up the turtle environment
turtle.speed(0)
turtle.bgcolor('lightblue')
turtle.title('Rainbow Pattern')
turtle.setup(700, 700)
turtle.colormode(1.0)  # Set color mode to 1.0 for float RGB values

num_colors = 49
radius = 300
penwidth = 20 * 7 / num_colors
hue = 0

for i in range(num_colors):
    (r, g, b) = colorsys.hsv_to_rgb(hue, 1, 1)
    draw_one_colour_arc(0, -100, radius, penwidth, (r, g, b))
    radius -= (penwidth - 1)
    hue += 0.9 / num_colors

turtle.done()



