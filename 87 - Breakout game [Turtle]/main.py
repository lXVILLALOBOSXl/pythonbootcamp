from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from brick import Brick
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle((0, -250))
ball = Ball()
scoreboard = Scoreboard()
bricks = []

def initialize_bricks():
    for x in range(-250, 289, 49):
        for y in range(250, 40, -30):
            brick = Brick((x, y))
            bricks.append(brick)

initialize_bricks()
screen.listen()
screen.onkey(paddle.go_left, "Left")
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "a")
screen.onkey(paddle.go_right, "d")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.xcor() > 250 or ball.xcor() < -250:
        ball.bounce_x()

    if ball.ycor() > 250:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.ycor() < -230 and -50 < ball.xcor() - paddle.xcor() < 50 and ball.y_move < 0:
        ball.bounce_y()

    # Detect collision with bricks
    for brick in bricks:
        if ball.distance(brick) < 20:
            # Get brick and ball position
            ball_x, ball_y = ball.xcor(), ball.ycor()
            brick_x, brick_y = brick.xcor(), brick.ycor()

            # Calculate the difference between the ball and the brick x and y positions
            diff_x = abs(ball_x - brick_x)
            diff_y = abs(ball_y - brick_y)

            # check if the ball is hitting the brick from the top or bottom
            if diff_x > diff_y:
                ball.bounce_x()  
            else:
                ball.bounce_y()  

            # Remove the brick from the screen and update the score
            brick.hideturtle()
            bricks.remove(brick)
            scoreboard.point()

    # Detect game over 
    if ball.ycor() < -270:
        ball.reset()
        paddle.reset_position()
        initialize_bricks()
        scoreboard.print("Game Over")
        time.sleep(2)
        scoreboard.save()
        scoreboard.reset()

    # Up level
    if len(bricks) == 0:
        ball.reset_position()
        paddle.reset_position()
        initialize_bricks()
        scoreboard.print("Level Up!")
        time.sleep(2)
        ball.move_speed *= 0.9


screen.exitonclick()