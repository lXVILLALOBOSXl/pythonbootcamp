from turtle import Screen, Turtle
from snake import Snake
from food import Food
import time

screen = Screen()
text = Turtle()
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake(length=3, color="white")
food = Food()


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
screen.onkey(key="s", fun=move_down)
screen.onkey(key="a", fun=move_left)
xn = int(round(screen.window_width() / 2) * -1) - 2
xp = int(round(screen.window_width() / 2)) - 5
yn = int(round(screen.window_height() / 2) * -1) + 2
yp = int(round(screen.window_height() / 2)) + 2
score = 0


def update_score():
    text.clear()
    text.penup()
    text.hideturtle()
    text.color("white")
    text.goto(0, screen.window_height() // 2 - 20)
    text.write(f"Score: {score}", align="center", font=("Arial", 16, "normal"))


def game_over():
    text.clear()
    text.write(f"Game over, score: {score}", align="center", font=("Arial", 16, "normal"))


update_score()
is_game_on = True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    if snake.body[0].part.distance(food) < 15:
        food.refresh()
        snake.grow()
        score += 1
        update_score()

    # detect collision with wall
    if snake.body[0].part.xcor() > xp or snake.body[0].part.xcor() < xn or snake.body[
        0].part.ycor() > yp or snake.body[0].part.ycor() < yn:
        print(snake.body[0].part.ycor())
        is_game_on = False
        game_over()

    # detect collision with tail
    for i in range(1, snake.length):
        if snake.body[0].part.distance(snake.body[i].part) < 15:
            is_game_on = False
            game_over()

screen.exitonclick()
