import turtle

IMG_PATH = "day-025/day-025_project_usa_quiz/blank_states_img.gif"


def main():
    screen = turtle.Screen()
    screen.title("U.S States Game")
    screen.addshape(IMG_PATH)

    turtle.shape(IMG_PATH)

    screen.exitonclick()


def get_mouse_click_coor(x, y):
    """Used to work out where to put the name of a state"""
    print(x, y)


if __name__ == "__main__":
    main()