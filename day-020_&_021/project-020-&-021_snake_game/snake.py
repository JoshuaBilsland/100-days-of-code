from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.__segments = []
        self.create_snake()

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(pos)
            self.__segments.append(snake_segment)

    def move(self):
        # range(start, stop, step)
        for seg_num in range(len(self.__segments) - 1, 0, -1):
            new_x = self.__segments[seg_num - 1].xcor()
            new_y = self.__segments[seg_num - 1].ycor()
            self.__segments[seg_num].goto(new_x, new_y)
        self.__segments[0].forward(MOVE_DISTANCE)
