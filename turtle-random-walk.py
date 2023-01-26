from turtle import Turtle, Screen
import random

tom = Turtle()
screen = Screen()
screen.bgcolor("black")
tom.shape("arrow")
tom.color("blue")
tom.pensize(10)
tom.shapesize(1,1)
tom.speed(10)

def change_color():
    R = random.random()
    G = random.random()
    B = random.random()
    tom.color(R, G, B)


# this also works
# def location():
#      direction = ["right", "left"]
#      a = random.choice(direction)
#      if a == "right":
#          tom.right(90)
#      else :
#          tom.left(90)

direction = [0, 90, 180, 270]

for _ in range(500):
    change_color()
    # location()
    tom.setheading(random.choice(direction))
    tom.forward(30)


screen.exitonclick()
