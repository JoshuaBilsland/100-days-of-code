from turtle import Screen, Turtle
import time


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    starting_positions = [(0, 0), (-20, 0), (-40, 0)]
    snake_segments = []

    for pos in starting_positions:
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(pos)
        snake_segments.append(snake_segment)

    running = True
    while running:
        screen.update()
        time.sleep(1)
        # range(start, stop, step)
        for seg_num in range(len(snake_segments) - 1, 0, -1):
            new_x = snake_segments[seg_num - 1].xcor()
            new_y = snake_segments[seg_num - 1].ycor()
            snake_segments[seg_num].goto(new_x, new_y)
        snake_segments[0].forward(20)


    screen.exitonclick()


if __name__ == "__main__":
    main()
