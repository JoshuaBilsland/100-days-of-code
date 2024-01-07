from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def counter_clockwise():
    tim.setheading(tim.heading() + 5)


def clockwise():
    tim.setheading(tim.heading() - 5)


def main():
    screen.listen()
    screen.onkey(move_forwards, "w")
    screen.onkey(move_backwards, "s")
    screen.onkey(counter_clockwise, "a")
    screen.onkey(clockwise, "d")
    screen.exitonclick()


if __name__ == "__main__":
    main()
