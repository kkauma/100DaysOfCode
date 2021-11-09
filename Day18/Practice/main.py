import turtle as t
import random

tim = t.Turtle()

colors = ["green", "red", "blue", "orange", "wheat", "magenta",
          "DarkOrchid", "DeepSkyBlue"]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

# import heroes
#
# print(heroes.gen())
# tim = Turtle()
# tim.shape("turtle")
# tim.color("magenta")
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
# tim.forward(100)
# tim.left(90)
#
# screen = Screen()
# screen.exitonclick()