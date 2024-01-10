from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.__l_score = 0
        self.__r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.__l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(100, 200)
        self.write(self.__r_score, align="center", font=("Courier", 70, "normal"))

    def l_point(self):
        self.__l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.__r_score += 1
        self.clear()
        self.update_scoreboard()
