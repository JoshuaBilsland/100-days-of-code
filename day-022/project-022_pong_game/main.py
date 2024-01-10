from turtle import Screen, Turtle
from functools import partial
from paddle import Paddle
from ball import Ball
import time

def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    l_paddle = Paddle((-350, 0))
    r_paddle = Paddle((350, 0))


    ball = Ball()

    screen.listen()
    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    running = True
    while running:
        time.sleep(0.1)
        screen.update()
        ball.move()

    screen.exitonclick()


if __name__ == "__main__":
    main()
