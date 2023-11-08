import turtle
import turtle as t
import random

pencil = t.Turtle()
screen = t.Screen()
screen.setup(width=1000, height=1000)
x_limit = screen.window_width() // 2
y_limit = screen.window_height() // 2


########### Challenge 3 - Draw Shapes ########
def random_color():
    # Generate random values for red, green, and blue components
    r = random.random()  # Red component
    g = random.random()  # Green component
    b = random.random()  # Blue component

    return r, g, b  # Return a tuple representing the RGB color


def draw_circle(pencil1, color, radius):
    pencil1.color(color)
    pencil1.circle(radius)


def draw_triangle(pencil1, color, large):
    pencil1.color(color)
    for x in range(1, 3):
        pencil1.forward(large)
        pencil1.left(120)
    pencil1.forward(large)
    pencil1.left(120)


def draw_square(pencil1, color, large):
    pencil1.color(color)
    for x in range(1, 5):
        pencil1.forward(large)
        pencil1.left(90)


random_number = random.randint(5, 20)
for i in range(1, random_number):
    if i > 1:
        pencil.pendown()
    random_shape = random.randint(1, 3)
    if random_shape == 1:
        draw_square(pencil, random_color(), random.randint(10, 300))
    elif random_shape == 2:
        draw_triangle(pencil, random_color(), random.randint(10, 300))
    else:
        draw_circle(pencil, random_color(), random.randint(10, 300)/2)
    pencil.penup()
    pencil.goto(random.randint(-x_limit, x_limit), random.randint(-y_limit, y_limit))
