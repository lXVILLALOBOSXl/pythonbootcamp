import turtle as t
import random

pencil = t.Turtle()
screen = t.Screen()
min_x = -screen.window_width() // 2
max_y = screen.window_height() // 2


########### Challenge 3 - Draw Shapes ########
def random_color():
    # Generate random values for red, green, and blue components
    r = random.random()  # Red component
    g = random.random()  # Green component
    b = random.random()  # Blue component

    return r, g, b  # Return a tuple representing the RGB color


def draw_circle(pencil1, color, radius):
    pencil1.color(color)
    pencil1.begin_fill()  # Start the fill
    pencil1.circle(radius)
    pencil1.end_fill()  # End the fill


def maximum_circles(radius, space):
    width = screen.window_width()
    height = screen.window_height()

    i = 1
    total_distance = ((2 * space) + (radius * 4))
    while total_distance <= width:
        i += 1
        total_distance = ((space + (radius * 4) * i) + space)
    maximum_horizontal_circles = i

    i = 1
    total_distance = ((2 * space) + (radius * 4))
    while total_distance <= height:
        i += 1
        total_distance = ((space + (radius * 4) * i) + space)
    maximum_vertical_circles = i

    return maximum_horizontal_circles, maximum_vertical_circles


def draw_art(pencil, radius, space_between):
    horizontal_circles, vertical_circles = maximum_circles(radius, space_between)

    y_coordinate = max_y
    for y in range(0, vertical_circles - 1):
        y_coordinate -= (space_between * 4)
        x_coordinate = min_x
        for x in range(0, horizontal_circles - 1):
            x_coordinate += (space_between * 4)
            pencil.penup()
            pencil.goto(x_coordinate, y_coordinate)
            pencil.pendown()
            draw_circle(pencil, random_color(), radius)


radius = 3
draw_art(pencil, radius, space_between=radius)

screen.exitonclick()
