from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.__score = 0
        self.color("white")
        self.penup()
        self.goto(0, 265)
        self.display()
        self.hideturtle()

    def display(self):
        self.write(f"Score: {self.__score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.__score += 1
        self.clear()
        self.display()
