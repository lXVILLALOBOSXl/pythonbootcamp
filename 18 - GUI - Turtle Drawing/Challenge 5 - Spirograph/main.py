import turtle as t
import random

screen = t.Screen()
pencil = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


########### Challenge 5 - Spirograph ########
def write_spirograph(pencil, size, degrees, radius):
    for i in range(1, round((degrees / 2))):
        pencil.left(degrees)  # Turn right 1 degree
        pencil.forward(size)
        pencil.circle(radius, 180)
        pencil.left(degrees / 2)  # Turn right 1 degree
        pencil.forward(size * 2)


pencil.speed("fastest")
pencil.color(random_color())
write_spirograph(pencil, 100, 50, 10)
print("a")

screen.exitonclick()

