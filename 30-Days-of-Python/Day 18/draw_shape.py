import turtle as t
import random

malik = t.Turtle()
malik.shape("classic")
malik.speed(10)

colours = [
    "black",
    "dark blue",
    "deep sky blue",
    "turquoise",
    "lime",
    "dark green",
    "red",
    "dark orange",
]


def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        malik.forward(100)
        malik.right(angle)


for shape_side_n in range(3, 11):
    malik.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = t.Screen()
screen.exitonclick()
