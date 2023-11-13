from turtle import Turtle, Screen
import random

screen = Screen()

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(int((screen.window_width() / 2) * -1) + 20, int((screen.window_width() / 2) - 20))
        random_y = random.randint(int((screen.window_height() / 2) * -1) + 20, int((screen.window_height() / 2) - 20))
        self.goto(x=random_x, y=random_y)
