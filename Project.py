
from mySquare import *
from random import randint
import turtle
bob = turtle.Turtle()
turtle.colormode(255)
bob.speed(0)

turtle.tracer(0)
turtle.bgcolor("black")

for times in range(1000):
    bob.width("5")
    x = randint(-800,800)
    y = randint(-400,400)
    s = randint(4,10)
    bob.color("lime green")
    bob.begin_fill()
    bob.color("red")
    move(bob,x,y)
    polygon(bob,10,13)
    bob.end_fill()


for times in range(73):
    bob.color("aqua")
    move(bob,10,20)
    bob.forward(1000)
    bob.right(5)
    polygon(bob,400,4)
    bob.width("8")


    
for times in range(181):
    bob.color(255,255,255)
    bob.forward(100)
    bob.right(30)
    bob.forward(10)
    bob.left(60)
    bob.forward(100)
    bob.right(30)
    
    bob.penup()
    bob.setposition(0, 0)
    bob.pendown()
    
    bob.right(2)

for times in range(180):
    bob.color(255,0,0)
    bob.forward(100)
    bob.right(30)
    bob.forward(5)
    bob.left(60)
    bob.forward(50)
    bob.right(30)
    
    bob.penup()
    bob.setposition(0, 0)
    bob.pendown()
    
    bob.right(2)

for times in range(180):
    bob.color(0,0,0)
    bob.forward(100)
    bob.right(30)
    bob.forward(5)
    bob.left(60)
    bob.right(30)
    
    bob.penup()
    bob.setposition(0, 0)
    bob.pendown()
    
    bob.right(2)

for times in range(180):
    bob.color(0,0,255)
    bob.forward(100)
    bob.right(30)
    bob.forward(10)
    bob.left(60)

    
    bob.penup()
    bob.setposition(0, 0)
    bob.pendown()
    
    bob.right(2)







