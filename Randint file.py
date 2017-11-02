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
