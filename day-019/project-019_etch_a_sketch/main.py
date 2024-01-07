from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def main():
    running = True
    while running:
        screen.listen()
        screen.onkey(move_forwards, "w")


if __name__ == "__main__":
    main()