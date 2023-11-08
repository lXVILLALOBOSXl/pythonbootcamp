import turtle as t
import random

pencil = t.Turtle()
screen = t.Screen()
screen.setup(width=500, height=500)
limit = screen.window_width() // 2

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
random_number = random.randint(50, 100)
for i in range(1, random_number):
    pencil.color(random.choice(colours))
    random_movement = random.randint(1, 4)

    # Get the current turtle position
    current_x, current_y = pencil.pos()

    if random_movement == 1:
        new_x = current_x + random.randint(-limit, limit)
        new_y = current_y + random.randint(-limit, limit)
        # Check if the new position is within the screen bounds
        if -limit < new_x < limit and -limit < new_y < limit:
            pencil.goto(new_x, new_y)
    elif random_movement == 2:
        new_x = current_x - random.randint(-limit, limit)
        new_y = current_y - random.randint(-limit, limit)
        # Check if the new position is within the screen bounds
        if -limit < new_x < limit and -limit < new_y < limit:
            pencil.goto(new_x, new_y)
    elif random_movement == 3:
        angle = random.randint(1, 360)
        pencil.left(angle)
    else:
        angle = random.randint(1, 360)
        pencil.right(angle)

