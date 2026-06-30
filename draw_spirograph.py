import turtle as t
import random

malik = t.Turtle()
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


malik.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        malik.color(random_color())
        malik.circle(100)
        malik.setheading(malik.heading() + size_of_gap)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
