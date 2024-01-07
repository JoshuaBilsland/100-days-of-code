from turtle import Turtle, Screen


def main():
    screen.exitonclick()


if __name__ == "__main__":
    tim = Turtle()
    screen = Screen()
    screen.setup(width=500, height=400)
    screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
    main()
