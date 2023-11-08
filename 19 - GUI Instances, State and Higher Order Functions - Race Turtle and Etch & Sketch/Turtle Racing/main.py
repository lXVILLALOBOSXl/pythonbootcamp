import random
from turtle import Turtle, Screen

pencil = Turtle()
pencil.hideturtle()
pencil.penup()
screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")


def new_player(color, shape):
    player = Turtle()
    player.shape(shape)
    player.color(color)
    player.speed(3)
    return player


# Function to display a message on the screen
def display_message(message):
    pencil.penup()
    pencil.goto(0, 0)  # Adjust coordinates if needed
    pencil.write(message, align="center", font=("Arial", 16, "normal"))


def set_turtles(turtles):
    y = (screen.window_height() / 2) - 30
    for turtle in turtles:
        turtle.penup()
        turtle.goto(((screen.window_width() / 2) * -1) + 9, y)
        y -= 30
        turtle.pendown()


def someone_wins(players):
    for player in players:
        if int(player.xcor()) >= int((screen.window_width() / 2) - 32):
            return player
    return None


def move_random(players):
    for player in players:
        player.penup()
        player.forward(random.randint(1, 10))


def turtles_race(turtles, bet):
    set_turtles(turtles)
    winner = someone_wins(players=turtles)
    while winner is None:
        move_random(turtles)
        winner = someone_wins(players=turtles)
    if winner.pencolor() == bet:
        return True
    return False


players = [new_player("red", shape="turtle"), new_player("orange", shape="turtle"),
           new_player("yellow", shape="turtle"), new_player("green", shape="turtle"),
           new_player("blue", shape="turtle"),
           new_player("indigo", shape="turtle"), new_player("violet", shape="turtle")]
if turtles_race(players, user_bet):
    pass
    display_message("Congratulations, you win!")
else:
    pass
    display_message("Sorry, you lose:(")

screen.exitonclick()
