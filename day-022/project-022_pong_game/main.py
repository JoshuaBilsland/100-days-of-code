from turtle import Screen, Turtle
from functools import partial

def go_up(paddle):
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def go_down(paddle):
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Pong")
    screen.tracer(0)

    paddle = Turtle()
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(350, 0)

    screen.listen()
    screen.onkey(partial(go_up, paddle), "Up")
    screen.onkey(partial(go_down, paddle), "Down")

    running = True
    while running:
        screen.update()

    screen.exitonclick()


if __name__ == "__main__":
    main()
