import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

text = turtle.Turtle()
text.hideturtle()
text.penup()
text.color("black")

data = pandas.read_csv("50_states.csv")
num_states = len(data)
answered_states = 0

answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name? : ")

while len(data) > 1:

    expected_state = data[data.state.str.lower() == answer_state.lower()]

    if answer_state == "exit":
        missing_states = [state for state in data.state]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if len(expected_state) > 0:
        answered_states += 1
        data = data[data.state.str.lower() != answer_state.lower()]
        text.goto(x=float(expected_state["x"]), y=float(expected_state["y"]))
        text.write(str(expected_state.iloc[0]["state"]))

    answer_state = screen.textinput(title=f"{answered_states}/{num_states}", prompt="What's another state's name? : ")

screen.exitonclick()
