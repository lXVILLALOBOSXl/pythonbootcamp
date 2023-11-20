from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")

snake = Snake(length=3, color="white")

def move_up():
    snake.turn("up")

def move_down():
    snake.turn("down")

def move_right():
    snake.turn("right")

def move_left():
    snake.turn("left")

screen.listen()
screen.onkey(key="w", fun=move_up)
screen.onkey(key="d", fun=move_right)
screen.onkeypress(key="s", fun=move_down)
screen.onkey(key="a", fun=move_left)

while True:
    snake.move()
    screen.update()
    time.sleep(0.2)

screen.exitonclick()
