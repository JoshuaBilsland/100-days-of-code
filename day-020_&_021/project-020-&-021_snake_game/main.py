from turtle import Screen, Turtle
from snake import Snake
import time


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()

    running = True
    while running:
        screen.update()
        time.sleep(0.1)
        snake.move()

    screen.exitonclick()


if __name__ == "__main__":
    main()
