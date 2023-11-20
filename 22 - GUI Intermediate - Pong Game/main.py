from game import Pong
import time

game = Pong()
while not game.game_over:
    game.refresh()
    time.sleep(0.2)
game.exit()
