from turtle import Turtle
class Part:
    def __init__(self, color, shape):
        self.part = Turtle()
        self.part.color(color)
        self.part.shape(shape)
        self.part.penup()
        self.part.speed("fastest")


class Snake:
    def __init__(self, length, color):
        self.length = length
        self.color = color
        self.body = []
        for i in range(0, self.length):
            self.body.append(Part(color=color, shape="square"))
        self.body[0].part.color("red")

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].part.xcor()
            new_y = self.body[i - 1].part.ycor()
            self.body[i].part.goto(new_x, new_y)

        self.body[0].part.forward(20)

    def turn(self, direction):
        if direction == "up" and self.body[0].part.heading() != 270:
            self.body[0].part.setheading(90)
        elif direction == "right" and self.body[0].part.heading() != 180:
            self.body[0].part.setheading(0)
        elif direction == "down" and self.body[0].part.heading() != 90:
            self.body[0].part.setheading(270)
        elif direction == "left" and self.body[0].part.heading() != 0:
            self.body[0].part.setheading(180)

