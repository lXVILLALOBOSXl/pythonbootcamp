from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.goto(position)

    def reset_position(self):
        self.goto(0, -250)

    def go_right(self):
        new_x = self.xcor() + 20
        if new_x < 250:
            self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        if new_x > -250:
            self.goto(new_x, self.ycor())
