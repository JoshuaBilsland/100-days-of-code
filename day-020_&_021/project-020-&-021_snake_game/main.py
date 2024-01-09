from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def main():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("My Snake Game")
    screen.tracer(0)

    snake = Snake()
    food = Food()
    scoreboard = Scoreboard()

    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")

    running = True
    while running:
        screen.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        if snake.get_head().distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Detect collision with wall
        if snake.get_head().xcor() > 280 or snake.get_head().xcor() < -280 or snake.get_head().ycor() > 280 or snake.get_head().ycor() < -280:
            running = False
            scoreboard.game_over()

        # Detect collision with tail
        for segment in snake.get_segments():
            if segment == snake.get_head():
                pass
            elif snake.get_head().distance(segment) < 10:
                running = False
                scoreboard.game_over()

    screen.exitonclick()


if __name__ == "__main__":
    main()
