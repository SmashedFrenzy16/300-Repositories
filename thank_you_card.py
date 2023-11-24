from turtle import *
from random import randint
import random

pen = Turtle()
pen.speed("normal")
s = Screen()
s.setup(width=1200, height=700)

colormode(255)

global colors

colors = ["red", "blue", "yellow", "green", "lightgreen", "purple", "pink"]

global rand_colors


def party_face():

    style = ('Courier', 20, 'normal')
    pen.write("🥳", font=style, align='center')

def write_300():

    style = ('Courier', 20, 'normal')
    pen.write("300!", font=style, align='center')

def fireworks_emoji():

    style = ('Courier', 20, 'normal')
    pen.write("🎆", font=style, align='center')

def text():

    pen.penup()

    pen.home()

    pen.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))

    pen.pendown()


    style = ('Courier', 20, 'normal')
    pen.write('Thank you to the GitHub community for helping me get to 300 repositories!', font=style, align='center')
    pen.hideturtle()


for i in range(20):

    pen.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))

    pen.penup()

    pen.goto(randint(-500, 500), randint(-300, 270))

    pen.pendown()

    party_face()

    pen.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))

    pen.penup()

    pen.goto(randint(-500, 500), randint(-300, 270))

    pen.pendown()

    write_300()

    pen.color(randint(0, 255),
              randint(0, 255),
              randint(0, 255))

    pen.penup()

    pen.goto(randint(-500, 500), randint(-300, 270))

    pen.pendown()

    fireworks_emoji()

text()

while True:
    s.update()