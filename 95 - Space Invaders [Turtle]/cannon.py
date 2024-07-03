import turtle
from turtle import Turtle
from projectile import Projectile

class Cannon(Turtle):

    CANNON_STEP = 10
    FLOOR_LEVEL = -250

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.lives = 3
        self.can_fire = True
        self.projectile = None
        self.penup()
        self.color(1, 1, 1)
        self.shape("square")
        self.setposition(0, self.FLOOR_LEVEL)
        self.turtlesize(0.5, 2)  
        self.stamp()
        self.sety(self.FLOOR_LEVEL + 5)  
        self.turtlesize(0.5, 0.75)  
        self.stamp()
        self.sety(self.FLOOR_LEVEL + 10)  
        self.turtlesize(0.4, 0.15) 
        self.stamp()
        self.sety(self.FLOOR_LEVEL)

    def draw_cannon(self):
        self.clear()
        self.turtlesize(0.5, 2)  
        self.stamp()
        self.sety(self.FLOOR_LEVEL + 5)  
        self.turtlesize(0.5, 0.75) 
        self.stamp()
        self.sety(self.FLOOR_LEVEL + 10) 
        self.turtlesize(0.4, 0.15) 
        self.stamp()
        self.sety(self.FLOOR_LEVEL)

    def restart_position(self):
        self.setposition(0, self.FLOOR_LEVEL)
        self.draw_cannon()

    def move_left(self):
        if self.xcor() <= -280:
            return
        self.setx(self.xcor() - self.CANNON_STEP)
        self.draw_cannon()

    def move_right(self):
        if self.xcor() >= 270:
            return
        self.setx(self.xcor() + self.CANNON_STEP)
        self.draw_cannon()

    def fire(self):
        if self.can_fire: 
            self.can_fire = False
            self.projectile = Projectile(self.xcor(), self.ycor() + 10, "white")
            self._move_projectile()

    def _move_projectile(self):
        if not self.projectile.check_collision():
            self.projectile.move(down=False)
            turtle.ontimer(lambda: self._move_projectile(), 20)
        else:
            self.projectile.destroy()
            self.can_fire = True
