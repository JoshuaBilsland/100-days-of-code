import turtle as t

tim = t.Turtle()

########### Challenge 2 - Draw a Dashed Line ########
for movement in range(50):
    tim.forward(5)
    tim.penup()
    tim.forward(5)
    tim.pendown()