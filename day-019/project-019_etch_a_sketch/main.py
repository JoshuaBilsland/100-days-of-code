from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def main():
    screen.listen()
    screen.onkey(fun=move_forwards, key="w")
    screen.onkey(move_backwards, "s")
    screen.exitonclick()


if __name__ == "__main__":
    main()
