from turtle import Turtle


class Trench(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.life = 35
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(position)
        self.shapesize(stretch_wid=2, stretch_len=3)

    def damage(self):
        self.life -= 1
        if self.life == 0:
            self.hideturtle()
            self.destroy()
        elif self.life == 10:
            self.color("red")
        elif self.life == 20:
            self.color("orange")
        elif self.life == 30:
            self.color("yellow")

    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()
        self.clear()

