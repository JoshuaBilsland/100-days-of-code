from turtle import Screen, Turtle


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")

    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    for pos in starting_positions:
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.goto(pos)


    screen.exitonclick()


if __name__ == "__main__":
    main()
