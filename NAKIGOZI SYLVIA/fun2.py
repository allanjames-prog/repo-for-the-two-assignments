
import turtle
import random

def draw_tree(t, branch_length, angle, shrink_factor, min_length):
    if branch_length > min_length:
        t.forward(branch_length)
        t.left(angle)
        draw_tree(t, branch_length * shrink_factor, angle, shrink_factor, min_length)
        t.right(angle * 2)
        draw_tree(t, branch_length * shrink_factor, angle, shrink_factor, min_length)
        t.left(angle)
        t.backward(branch_length)

def draw_leaves(t, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("#3E8E41")  # green
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    t.color("#964B00")  # brown
    t.width(1)
    t.penup()
    t.goto(x - 5, y + 5)
    t.pendown()
    t.forward(10)
    t.penup()
    t.goto(x + 5, y + 5)
    t.pendown()
    t.forward(10)

def main():
    t = turtle.Turtle()
    t.speed(0)  # fastest speed
    t.left(90)

    # Draw multiple trees
    for i in range(5):
        for j in range(5):
            x = i * 100 - 200
            y = j * 100 - 200
            branch_length = random.randint(50, 150)

            t.penup()
            t.goto(x, y)
            t.pendown()

            t.color("#786C3B")  # brown
            t.width(5)
            t.forward(branch_length)

            t.color("#3E8E41")  # green
            t.width(2)
            draw_tree(t, branch_length, 30, 0.7, 5)

            draw_leaves(t, x + branch_length, y + branch_length)
            draw_leaves(t, x - branch_length, y + branch_length)
            draw_leaves(t, x, y + branch_length + 20)

    turtle.done()

main()
