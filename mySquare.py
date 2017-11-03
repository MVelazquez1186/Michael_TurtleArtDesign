def square( t, distance ):
    for times in range(4):
        t.forward(100)
        t.left(90)

def triangle( t, distance ):
    for times in range(3):
        t.forward(100)
        t.left(120)

def polygon( t, distance, side):
    angle = 360 / side
    for times in range(side):
        t.forward(distance)
        t.left(angle)
    

def move( t, x, y):
    t.penup()
    t.goto(x,y)
    t.pendown()

from random import randint
from mySquare import *
import turtle
turtle.colormode(255)

bob = turtle.Turtle()
bob.speed(0)

for times in range(1000):
    x = randint(-600,600)
    y = randint(-400,400)
    s = randint(4,10)
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    bob.color(red,green,blue)
    move(bob,x,y)
    polygon(bob,20,s)


 


