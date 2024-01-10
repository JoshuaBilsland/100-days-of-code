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

        # Detect collision with top/bottom wall
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce_y()
            
        # Detect collision with paddle
        if ((ball.distance(r_paddle) < 50 and ball.xcor() > 320) or
                (ball.distance(l_paddle) < 50 and ball.xcor() < -320)):
            ball.bounce_x()

    screen.exitonclick()


if __name__ == "__main__":
    main()
