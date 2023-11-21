import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(180)
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=1.25)
        random_color = random.choice(COLORS)
        self.color(random_color)
        new_y = random.randint(-260, 260)
        new_x = random.randint(-300, 300)
        self.goto(x=new_x, y=new_y)

    def move(self, pace):
        self.forward(pace)

    def regenerate(self):
        new_y = random.randint(-260, 260)
        self.goto(x=300, y=new_y)


def move_faster():
    global STARTING_MOVE_DISTANCE  # Declare the variable as global
    STARTING_MOVE_DISTANCE += MOVE_INCREMENT


class CarManager:
    def __init__(self):
        self.cars = []
        for i in range(0, 30, 1):
            self.cars.append(Car())

    def move(self):
        for car in self.cars:
            car.move(STARTING_MOVE_DISTANCE)
            if car.xcor() < -300:
                car.regenerate()

    def run_over(self, player):
        for car in self.cars:
            if abs(player.ycor() - car.ycor()) < 18 and abs(player.xcor() - car.xcor()) < 18:
                return True
