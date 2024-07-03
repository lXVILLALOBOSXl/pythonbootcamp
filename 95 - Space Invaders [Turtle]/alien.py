import turtle
from turtle import Turtle
from projectile import Projectile


from turtle import Turtle

class Alien(Turtle):

    ALIEN_STEP = 5

    def __init__(self, position, color):
        super().__init__()
        self.can_fire = True
        self.projectile = None
        self.shape("turtle")
        self.right(90)
        self.color(color)
        if color == "green":
            self.points = 5
        elif color == "lime":
            self.points = 2
        else:
            self.points = 1
        self.penup()
        self.goto(position)

    def destroy(self):
        self.goto(1000, 1000)
        self.hideturtle()
        self.clear()
        return self.points

    def move_left(self):
        self.setx(self.xcor() - self.ALIEN_STEP)

    def move_right(self):
        self.setx(self.xcor() + self.ALIEN_STEP)


    def move_down(self):
        if self.ycor() <= -280:
            return
        self.sety(self.ycor() - self.ALIEN_STEP)

    

    def fire(self):
        if self.can_fire: 
            self.can_fire = False
            self.projectile = Projectile(self.xcor(), self.ycor() - 10, "red")
            self._move_projectile()

    def _move_projectile(self):
        if not self.projectile.check_collision():
            self.projectile.move(down=True)
            turtle.ontimer(lambda: self._move_projectile(), 20)
        else:
            self.projectile.destroy()
            self.can_fire = True


    