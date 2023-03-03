import turtle
import math
import random
from turtle import *

title("Turtle Archery")
setup(width=0.3, height=.9, startx=None, starty=0)
bgcolor("skyblue")
build = Turtle()
arrow1 = Turtle()
arrow2 = Turtle()
arrow3 = Turtle()
arrow1.penup()
arrow2.penup()
arrow3.penup()

delay(0)
# build.hideturtle()
build.speed(0)
build.penup()
build.setpos(0, 425)
build.write("Turtle Archery", False, align="center", font=('Arial', 20, 'bold'))
build.setpos(0, 200)
build.dot(403, 'black')
build.dot(400, 'white')
build.dot(320, 'black')
build.dot(240, 'skyblue')
build.dot(163, 'black')
build.dot(160, 'red')
build.dot(83, 'black')
build.dot(80, 'yellow')
build.dot(33, 'black')
build.dot(30, 'yellow')
build.setpos(-225, -280)
build.write("Arrows left", False, align="center", font=("Arial", 12))
arrow2.setpos(-240, -300)
arrow3.setpos(-210, -300)
# build.fillcolor("white")
# build.begin_fill()
# build.circle(200)
# build.end_fill()





turtle.done()