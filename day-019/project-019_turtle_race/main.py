from turtle import Turtle, Screen
import random


def main(colours, user_bet):
    turtles = []
    y_positions = [-70, -40, -10, 20, 50, 80]
    pos_index = 0
    for colour in colours:
        turtle = Turtle(shape="turtle")
        turtle.color(colour)
        turtles.append(turtle)
        turtle.penup()
        turtle.goto(x=-230, y=y_positions[pos_index])
        pos_index += 1

    race_on = True
    while race_on:
        for turtle in turtles:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)
            if turtle.xcor() > 230:  # Check if it has won (by reaching the other side of screen)
                race_on = False
                winning_colour = turtle.pencolor()
                if winning_colour == user_bet:
                    print(f"You've won! The {winning_colour} turtle is the winner!")
                else:
                    print(f"You've lost! The {winning_colour} turtle is the winner!")

    screen.exitonclick()


if __name__ == "__main__":
    colours = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "purple"
    ]
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? {colours} Enter a colour: ")
    main(colours, user_bet)
