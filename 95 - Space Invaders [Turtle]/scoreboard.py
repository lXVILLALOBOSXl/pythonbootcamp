from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = lives
        with open("best_score.txt") as file:
            self.best_score = int(file.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(260, 268)
        self.write(f"S: {self.score}", align="center", font=("Courier", 15, "normal"))
        self.goto(-260, 268)
        self.write(f"BS: {self.best_score}", align="center", font=("Courier", 15, "normal"))
        self.goto(0, 268)
        self.write(f"Lives: {self.lives}", align="center", font=("Courier", 15, "normal"))

    def print(self, message):
        self.goto(0, 0)
        self.write(message, align="center", font=("Courier", 30, "normal"))

    def reset(self):
        self.score = 0
        self.update_scoreboard()

    def point(self):
        self.score += 1
        self.update_scoreboard()

    def save(self):
        if self.score > self.best_score:
            self.best_score = self.score
            with open("best_score.txt", mode="w") as file:
                file.write(str(self.best_score))
