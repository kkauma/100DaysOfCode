import turtle as t
import random

# Create a turtle instance
tim = t.Turtle()

colors = ["green", "red", "blue", "orange", "wheat", "magenta",
          "DarkOrchid", "DeepSkyBlue"]
directions = [0, 90, 180, 270]
tim.pensize(15)

# Draw a Random Walk - Challenge
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))

# Create a draw shape function
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# # Loop over shape a user defined number of times
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colors))
#     draw_shape(shape_side_n)


