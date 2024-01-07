from turtle import Turtle, Screen


def main(colours):
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
    screen.textinput(title="Make your bet", prompt=f"Which turtle will win the race? {colours} Enter a colour: ")
    main(colours)
