from turtle import Screen
from cannon import Cannon
from scoreboard import Scoreboard
from alien import Alien
from trench import Trench
import random
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Space Invaders Game")
screen.tracer(0)

cannon = Cannon()
scoreboard = Scoreboard(cannon.lives)
aliens = []
trenches = []

def initialize_aliens():
    for x in range(-190, 190, 35):
        for y_index, y in enumerate(range(190, 40, -30)):
            if y_index == 0:
                alien_color = "green"
            elif y_index in [1, 2]:
                alien_color = "lime"
            elif y_index in [3, 4]:
                alien_color = "pale green"
            alien = Alien((x, y), alien_color)
            aliens.append(alien)

def initialize_trenches():
    for x in range(-190, 190, 120):
        for y in range(-190, -160, 70):
            trench = Trench((x, y))
            trenches.append(trench)

initialize_aliens()
initialize_trenches()

direction = "right"

def move_aliens_horizontal(aliens):
    global direction

    if direction == "right":
        touching_border = any(alien.xcor() >= 270 for alien in aliens)
        if touching_border:
            direction = "left"
            for alien in aliens:
                alien.move_left()  # Move down when hitting the border
        else:
            for alien in aliens:
                alien.move_right()
    elif direction == "left":
        touching_border = any(alien.xcor() <= -280 for alien in aliens)
        if touching_border:
            direction = "right"
            for alien in aliens:
                alien.move_right()  # Move down when hitting the border
        else:
            for alien in aliens:
                alien.move_left()

def move_aliens_down(aliens):
    touching_border = any(alien.ycor() <= -145 for alien in aliens)
    if not touching_border:
        for alien in aliens:
            alien.move_down()
    else:
        pass

def detect_collisions():
    if cannon.projectile:
        for trench in trenches:
            if trench.distance(cannon.projectile) < 20:
                cannon.projectile.destroy()
                trench.damage()

        for alien in aliens:
            if alien.distance(cannon.projectile) < 20:
                cannon.projectile.destroy()
                points = alien.destroy()
                scoreboard.score += points
                scoreboard.update_scoreboard()
                aliens.remove(alien)
                if len(aliens) == 0:
                    cannon.lives += 2
                    scoreboard.lives = cannon.lives
                    scoreboard.update_scoreboard()
                    initialize_aliens()
                    initialize_trenches()
                    cannon.restart_position()
    for alien in aliens:
        if alien.projectile:
            if cannon.distance(alien.projectile) < 20:
                alien.projectile.destroy()
                cannon.lives -= 1
                scoreboard.lives = cannon.lives
                scoreboard.update_scoreboard()
                cannon.restart_position()

            for trench in trenches:
                if trench.distance(alien.projectile) < 20:
                    alien.projectile.destroy()
                    trench.damage()

screen.listen()
screen.onkey(cannon.move_left, "Left")
screen.onkey(cannon.move_right, "Right")
screen.onkey(cannon.move_left, "a")
screen.onkey(cannon.move_right, "d")
screen.onkey(cannon.fire, "space")
screen.onkey(cannon.fire, "Up")
screen.onkey(cannon.fire, "w")

start_time = time.time()
start_time_fire = time.time()

last_move_time = time.time()
move_interval = 0.2 
fire_interval = 1

while cannon.lives > 0:
    now = time.time()
    
    if now - last_move_time > move_interval:
        if now - start_time > 10:
            move_aliens_down(aliens)
            start_time = now
        move_aliens_horizontal(aliens)
        last_move_time = now 

    if now - start_time_fire > fire_interval:
        random_alien = random.choice(aliens)
        random_alien.fire()
        start_time_fire = now

    detect_collisions()
    
    screen.update()

if scoreboard.score > scoreboard.best_score:
    scoreboard.save()
    scoreboard.print(f"New High Score: {scoreboard.score}")
else:
    scoreboard.print(f"Game Over! Your Score: {scoreboard.score}")

screen.exitonclick()
