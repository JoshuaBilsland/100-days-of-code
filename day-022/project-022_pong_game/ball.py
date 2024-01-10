from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.__x_move = 10
        self.__y_move = 10

    def move(self):
        new_x = self.xcor() + self.__x_move
        new_y = self.ycor() + self.__y_move
        self.goto(new_x, new_y)

    def bounce(self):
        # Reverse direction
        self.__y_move *= -1
