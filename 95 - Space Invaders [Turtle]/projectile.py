from turtle import Turtle

class Projectile(Turtle):

    def __init__(self, start_x, start_y, color):
        super().__init__()
        self.speed("fastest")
        self.shape("circle")
        self.color(color)
        self.penup()
        self.setposition(start_x, start_y)
        self.turtlesize(0.5)

    def move(self, down):
        if down:
            self.sety(self.ycor() - 3)
        else:
            self.sety(self.ycor() + 10)

    def check_collision(self):
        return self.ycor() > 260 or self.ycor() < -260
    
    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()
        self.clear()
