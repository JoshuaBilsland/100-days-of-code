from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.__segments = []
        self.create_snake()
        self.__head = self.__segments[0]

    def get_head(self):
        return self.__head

    def get_segments(self):
        return self.__segments

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, position):
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.__segments.append(snake_segment)

    def extend(self):
        self.add_segment(self.__segments[-1].position())

    def move(self):
        # range(start, stop, step)
        for seg_num in range(len(self.__segments) - 1, 0, -1):
            new_x = self.__segments[seg_num - 1].xcor()
            new_y = self.__segments[seg_num - 1].ycor()
            self.__segments[seg_num].goto(new_x, new_y)
        self.__head.forward(MOVE_DISTANCE)

    def up(self):
        if self.__head.heading() != DOWN:
            self.__head.setheading(UP)

    def down(self):
        if self.__head.heading() != UP:
            self.__head.setheading(DOWN)

    def left(self):
        if self.__head.heading() != RIGHT:
            self.__head.setheading(LEFT)

    def right(self):
        if self.__head.heading() != LEFT:
            self.__head.setheading(RIGHT)
