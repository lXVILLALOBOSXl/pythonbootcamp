import time
from turtle import Screen

import car_manager
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(key="w", fun=player.move_forward)
screen.onkey(key="a", fun=player.move_left)
screen.onkey(key="d", fun=player.move_right)

level = 1
scoreboard = Scoreboard(level)

traffic = CarManager()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    traffic.move()

    if traffic.run_over(player):
        game_is_on = False

    if player.reach_finish_line():
        level += 1
        scoreboard.update(level)
        player.reload()
        car_manager.move_faster()

screen.update()
scoreboard.game_over()
screen.exitonclick()
