import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="What's another state's name?"
    )

    if answer_state is None:
        break

    answer_state = answer_state.title()

    if answer_state == "Exit":
        break

    if answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)

        state_row = data[data.state == answer_state]
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(state_row.state.item(), align="center", font=("Arial", 8, "normal"))

missing_states = [state for state in all_states if state not in guessed_states]
missing_df = pandas.DataFrame(missing_states, columns=["state"])
missing_df.to_csv("states_learn.csv", index=False)

screen.exitonclick()