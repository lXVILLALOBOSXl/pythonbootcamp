from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self, level):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=-290, y=265)
        self.color("black")
        self.write(f"Level: {level}", font=FONT)

    def update(self, level):
        self.clear()
        self.write(f"Level: {level}", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game over",align="center", font=FONT)

