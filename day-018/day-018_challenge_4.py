import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["DeepPink",
           "DarkBlue",
           "azure4",
           "CadetBlue2",
           "BlueViolet",
           "DarkSalmon",
           "DarkGoldenrod1",
           "SeaGreen"]

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for movement in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))
