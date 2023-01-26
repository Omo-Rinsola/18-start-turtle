from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("arrow")


def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    tim.color(R, G, B)


# ALL
num_of_sides = 3
for _ in range(8):
    change_color()
    for sides in range(num_of_sides):
        tim.right(360 / num_of_sides)
        tim.forward(100)
    num_of_sides += 1


screen = Screen()
screen.exitonclick()
