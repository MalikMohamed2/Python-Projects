import turtle
import pandas
import os

base_dir = os.path.dirname(__file__)

# paths صح
image_path = os.path.join(base_dir, "blank_states_img.gif")
csv_path = os.path.join(base_dir, "50_states.csv")

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image_path)
turtle.shape(image_path)

data = pandas.read_csv(csv_path)
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?",
    ).title()

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv(os.path.join(base_dir, "states_to_learn.csv"))
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()

        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
