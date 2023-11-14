from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self, color):
        super().__init__()
        self.hideturtle()
        self.color(color)


class Racket(Turtle):
    def __init__(self, color, side, width, height):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.width(20)
        self.color(color)
        self.setheading(270)
        if side == "left":
            self.goto(x=((width / 2) * -1) + 20, y=(height / 8))
        else:
            self.goto(x=(width / 2) - 30, y=(height / 8))
        self.pendown()
        self.forward((height / 8) * 2)


class ScoreBoard(Turtle):
    def __init__(self, height, color, points_p1, points_p2):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=(height / 2) - 40)
        self.color(color)
        self.write(f"{points_p1}\t{points_p2}", align="center", font=("Arial", 26, "normal"))


class Player:
    def __init__(self, racket):
        self.racket = racket
        self.points = 0


class Pong:

    def __init__(self, court_color, items_color):
        self.is_over = False
        self._init_screen_(court_color, items_color)
        self.racket1 = Racket(items_color, "left", self.width, self.height)
        self.racket2 = Racket(items_color, "right", self.width, self.height)
        self.player1 = Player(self.racket1)
        self.player2 = Player(self.racket2)
        self.score_board = ScoreBoard(self.height, items_color, self.player1.points, self.player2.points)
        self.ball = Ball(items_color)

    def _init_screen_(self, color, net_color):
        self.screen = Screen()
        self.screen.delay(0)
        self.screen.bgcolor(color)
        self.screen.title("Pong Game")
        self.width = self.screen.window_width()
        self.height = self.screen.window_height()
        self._print_net(net_color)

    def _print_net(self, color):
        self.net = Turtle()
        self.net.hideturtle()
        self.net.width(20)
        self.net.color(color)
        self.net.penup()
        self.net.setheading(270)
        self.net.goto(x=0, y=self.height / 2)
        while self.net.ycor() >= (self.height / 2) * -1:
            self.net.pendown()
            self.net.forward(20)
            self.net.penup()
            self.net.forward(40)

    def refresh(self):
        self.screen.update()
