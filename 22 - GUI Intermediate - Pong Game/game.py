from turtle import Screen, Turtle

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen_height = screen.window_height()
screen_width = screen.window_width()


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")

    def move(self):
        pass


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
        if (self.ycor() - 20) - (screen_height / 6) >= (screen_height / 2)*-1:
            self.backward(20)


class Pong:
    def __init__(self):
        screen.tracer(0)
        paddle1 = Paddle("left")
        paddle2 = Paddle("right")
        screen.listen()
        screen.onkey(key="w", fun=paddle1.move_up)
        screen.onkey(key="s", fun=paddle1.move_down)
        screen.onkey(key="Up", fun=paddle2.move_up)
        screen.onkey(key="Down", fun=paddle2.move_down)
        ball = Ball()
        ball.move()
        self.game_over = False
        screen.update()
        # screen.exitonclick()

    def refresh(self):
        screen.update()

    def exit(self):
        screen.exitonclick()
