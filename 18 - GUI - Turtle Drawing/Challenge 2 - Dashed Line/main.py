import turtle as t

screen = t.Screen()
tim = t.Turtle()
tim.shape("turtle")


########### Challenge 2 - Draw a Dashed Line ########
def draw_dash_line(turtle, distance, color):
    turtle.color(color)
    turtle.forward(distance / 2)
    turtle.penup()
    turtle.forward(distance / 2)
    turtle.pendown()



for i in range(1, 51):
    draw_dash_line(tim, 10, "red")

screen.exitonclick()
