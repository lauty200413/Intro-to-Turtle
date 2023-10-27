import turtle
from turtle import Turtle, Screen
import random

merki = Turtle()
my_screen = Screen()


colors = ["CornFlowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen"]
angles = [90, -90, 0, 270]


turtle.colormode(255)

merki.hideturtle()
merki.width(15)
merki.speed(0)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


def square():

    merki.forward(100)
    merki.right(90)
    merki.forward(100)
    merki.right(90)
    merki.forward(100)
    merki.right(90)
    merki.forward(100)

def dashed_line():
    for i in range(20):
        merki.forward(15)
        merki.penup()
        merki.forward(15)
        merki.pendown()


def draw_shape(sides):
    angle = 360/sides
    for i in range(sides):
        merki.forward(150)
        merki.right(angle)


def random_walk():
    for i in range(50):
        merki.forward(30)
        merki.right(random.choice(angles))
        merki.color(random_color())

def draw_spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        merki.width(0)
        merki.color(random_color())
        merki.setheading(merki.heading() + size_of_gap)
        merki.circle(100)


draw_spirograph(100)

my_screen.exitonclick()
