from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto(STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        if not self.xcor() - 20 < -300:
            self.goto(x=self.xcor() - MOVE_DISTANCE, y=self.ycor())

    def move_right(self):
        if not self.xcor() + 30 > 300:
            self.goto(x=self.xcor() + MOVE_DISTANCE, y=self.ycor())

    def reach_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def reload(self):
        self.goto(STARTING_POSITION)
