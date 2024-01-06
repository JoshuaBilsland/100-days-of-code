###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram
import turtle
import random

# USED TO EXTRACT COLOURS

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r, g, b)
#     rgb_colors.append(new_colour)

# print(rgb_colors)


def draw_dots(tim, box_height, box_width, dot_size, dot_separation_size, colour_list):
    starting_pos = tim.position()
    tim.penup()
    for row in range(box_height):
        for dot in range(box_width):
            tim.dot(dot_size, random.choice(colour_list))
            tim.forward(dot_separation_size)
        tim.penup()
        tim.teleport(starting_pos[0], (starting_pos[1] - ((row + 1) * dot_separation_size)))


def main():
    colour_list = [(202, 164, 110),
                   (149, 75, 50),
                   (222, 201, 136),
                   (53, 93, 123),
                   (170, 154, 41),
                   (138, 31, 20),
                   (134, 163, 184),
                   (197, 92, 73),
                   (47, 121, 86),
                   (73, 43, 35),
                   (145, 178, 149),
                   (14, 98, 70),
                   (232, 176, 165),
                   (160, 142, 158),
                   (54, 45, 50),
                   (101, 75, 77),
                   (183, 205, 171),
                   (36, 60, 74),
                   (19, 86, 89),
                   (82, 148, 129),
                   (147, 17, 19),
                   (27, 68, 102),
                   (12, 70, 64),
                   (107, 127, 153),
                   (176, 192, 208),
                   (168, 99, 102)
                   ]

    turtle.colormode(255)
    tim = turtle.Turtle()
    tim.speed("fastest")
    tim.hideturtle()
    draw_dots(tim, 10, 10, 20, 50, colour_list)


if __name__ == "__main__":
    main()