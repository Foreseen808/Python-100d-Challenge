import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

d = pd.read_csv("50_states.csv")
state_list = d.state.to_list()
x_list = d.x.to_list()
y_list = d.y.to_list()

correct_guess = []
while len(correct_guess) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guess)}/50 States Correct",
                                    prompt="What's another state's name?")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        index = state_list.index(answer_state)
        t.goto(x=x_list[index], y=y_list[index])
        t.write(answer_state)
        correct_guess.append(answer_state)

# Exporting remaining states to CSV
states_remainder = set(state_list) - set(correct_guess)
states_remainder = [state for state in state_list if state not in correct_guess]
remaining_states = pd.DataFrame(sorted(states_remainder))
remaining_states.to_csv("states_to_learn.csv")
