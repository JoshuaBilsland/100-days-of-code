import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.__cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:  # Reduce the frequency of cars being created
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.__cars.append(car)

    def move_cars(self):
        for car in self.__cars:
            car.backward(STARTING_MOVE_DISTANCE)
