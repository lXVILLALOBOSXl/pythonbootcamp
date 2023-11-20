from turtle import Screen, Turtle
import math

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen_height = screen.window_height()
screen_width = screen.window_width()


class ScoreBoard(Turtle):
    def __init__(self, points_p1, points_p2):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=(screen_height / 2) - 40)
        self.color("white")
        self.write(f"{points_p1}\t{points_p2}", align="center", font=("Arial", 26, "normal"))

    def update(self, points_p1, points_p2):
        self.clear()
        self.write(f"{points_p1}\t{points_p2}", align="center", font=("Arial", 26, "normal"))


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(x=new_x,y=new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        if self.x_move > 0:
            self.x_move += 2
            self.y_move += 2
        else:
            self.x_move -= 2
            self.y_move -= 2
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.x_move = 10
        self.y_move = 10


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape("square")
        self.color("white")
        self.width = self.shapesize()[0] * 20  # 20 px is the default size of width and height's turtle
        self.height = (screen_height / (3 * self.shapesize()[0] * 20)) * 20
        self.shapesize(stretch_wid=self.width / 20, stretch_len=self.height / 20)
        if side == "right":
            self.setposition(x=(screen_width / 2) - 50, y=0)
        else:
            self.setposition(x=(screen_width / 2) * -1 + 40, y=0)

    def move_up(self):
        if (self.ycor() + 10) + (screen_height / 6) <= (screen_height / 2):
            self.forward(20)

    def move_down(self):
        if (self.ycor() - 20) - (screen_height / 6) >= (screen_height / 2) * -1:
            self.backward(20)


class Pong:
    def __init__(self):
        screen.tracer(0)
        self._print_net()
        self.paddle1 = Paddle("left")
        self.paddle2 = Paddle("right")
        screen.listen()
        screen.onkey(key="w", fun=self.paddle1.move_up)
        screen.onkey(key="s", fun=self.paddle1.move_down)
        screen.onkey(key="Up", fun=self.paddle2.move_up)
        screen.onkey(key="Down", fun=self.paddle2.move_down)
        self.ball = Ball()
        self.points_p1 = 0
        self.points_p2 = 0
        self.score_board = ScoreBoard(self.points_p1, self.points_p2)
        self.game_over = False
        screen.update()

    def _print_net(self):
        self.net = Turtle()
        self.net.hideturtle()
        self.net.width(20)
        self.net.color("white")
        self.net.penup()
        self.net.setheading(270)
        self.net.goto(x=0, y=screen_height / 2)
        while self.net.ycor() >= (screen_height / 2) * -1:
            self.net.pendown()
            self.net.forward(20)
            self.net.penup()
            self.net.forward(40)

    def refresh(self):
        #  Detect collision with the ball
        if self.ball.ycor() >= (screen_height / 2) - 20 or self.ball.ycor() <= ((screen_height / 2) * -1) + 20:
            self.ball.bounce_y()
        self.ball.move()

        #  Detect collision with the paddle
        if (self.ball.distance(self.paddle2) < 101 and self.ball.xcor() > (screen_width / 2) - 80) or (self.ball.distance(self.paddle1) < 101 and self.ball.xcor() < ((screen_width / 2) * -1) + 80):
            self.ball.bounce_x()

        #  Left paddle misses
        if self.ball.xcor() < ((screen_width / 2) * -1):
            self.points_p2 += 1
            self.score_board.update(self.points_p1, self.points_p2)
            self.ball.reset_position()

        #  Right paddle misses
        if self.ball.xcor() > (screen_width / 2):
            self.points_p1 += 1
            self.score_board.update(self.points_p1, self.points_p2)
            self.ball.reset_position()
        screen.update()

        if self.points_p1 > 7 or self.points_p2 > 7:
            self.ball.hideturtle()
            self.score_board.clear()
            self.score_board.write("Game \t Over", align="center", font=("Arial", 26, "normal"))
            self.game_over = True

    def exit(self):
        screen.exitonclick()
