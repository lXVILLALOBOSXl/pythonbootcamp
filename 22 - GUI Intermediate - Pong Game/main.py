from game import Pong
import time

game = Pong("black", "white")
while game.is_over is False:
    game.refresh()
    time.sleep(0.2)
