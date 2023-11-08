from turtle import Turtle, Screen

pencil = Turtle()
screen = Screen()
screen.listen()


def go_forward():
    pencil.forward(10)


def go_backward():
    pencil.backward(10)


def move_left():
    pencil.setheading(pencil.heading() - 10)


def move_right():
    pencil.setheading(pencil.heading() + 10)


def clear():
    pencil.clear()
    pencil.penup()
    pencil.home()
    pencil.pendown()


pencil.setheading(90)
screen.onkey(key="w", fun=go_forward)
screen.onkey(key="s", fun=go_backward)
screen.onkey(key="d", fun=move_left)
screen.onkey(key="a", fun=move_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
