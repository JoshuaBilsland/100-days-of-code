import turtle
import pandas

IMG_PATH = "day-025/day-025_project_usa_quiz/blank_states_img.gif"


def main():
    screen = turtle.Screen()
    screen.title("U.S States Game")
    screen.addshape(IMG_PATH)

    turtle.shape(IMG_PATH)
    data = pandas.read_csv("day-025/day-025_project_usa_quiz/50_states.csv")
    all_states = data.state.to_list()
    states_left_to_guess = all_states

    while len(states_left_to_guess) != 0:
        user_guess = screen.textinput(
            title=f"{50-len(states_left_to_guess)}/50 States Correct",
            prompt="What's another state's name"
        ).title()

        if user_guess == "Exit":
            break

        if user_guess in all_states:
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_row = data[data.state == user_guess]
            t.goto(int(state_row.x), int(state_row.y))
            t.write(user_guess)
            states_left_to_guess.remove(user_guess)

    states_remaining = pandas.DataFrame(states_left_to_guess)
    states_remaining.to_csv("day-025/day-025_project_usa_quiz/states_remaining.csv")
    screen.exitonclick()


def get_mouse_click_coor(x, y):
    """Used to work out where to put the name of a state"""
    print(x, y)


if __name__ == "__main__":
    main()