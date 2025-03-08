import turtle

import pandas
import pandas as pd

FONT = ("Arial", 12, "bold")

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")

correct_guess = []
total_states = len(data)

while len(correct_guess) < total_states:
    answer_state = screen.textinput(
        title=f"{len(correct_guess)}/{total_states} States Correct",
        prompt="What's another state's name?").title()

    if not answer_state:
        break
    elif answer_state == "Exit":
        missing_states = [state for state in data.state.to_list() if state not in correct_guess]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    states_list = data["state"]

    if answer_state in states_list.values and answer_state not in correct_guess:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_row = data[states_list == answer_state]

        t.goto(state_row.x.item(), state_row.y.item())
        t.write(answer_state)

        correct_guess.append(answer_state)
    elif answer_state in correct_guess:
        print("You already guessed that state!")
    else:
        print("Incorrect! Try again.")



turtle.mainloop()