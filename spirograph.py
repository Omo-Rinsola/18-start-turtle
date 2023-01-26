from turtle import Turtle, Screen
import random

tom = Turtle()
screen = Screen()
tom.shape("arrow")
tom.speed("fastest")
# tom.colormode(255)
def change_colour():
    r = random.random()
    g = random.random()
    b = random.random()
    return tom.color(r, g, b)

def  spiro(size_of_space):
    for _ in range (int(360 / size_of_space)):
        change_colour()
        tom.circle(100)
        current_heading = tom.heading()
        tom.setheading(current_heading + size_of_space)

spiro(5)

screen = Screen()
screen.exitonclick()