#!/usr/bin/env python2
#coding=utf-8

import turtle 
import random
turtle.title("Random polygon")
turtle.setup(10000,10000,0,0)


def draw_A_Polygon(number_Of_Sides, length):
    turtle.speed(10)
    color_fill = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    color_pen = '#{:02x}{:02x}{:02x}'.format(*map(lambda x: random.randint(0, 255), range(3)))
    turtle.fillcolor(color_fill)
    turtle.pencolor(color_pen)
    turtle.penup()
    turtle.goto(random.randint(-300,300),random.randint(-300,300))
    turtle.pendown()
    angle = 360.0/number_Of_Sides
    turtle.begin_fill()

    for i in range(number_Of_Sides):
        turtle.forward(length)
        turtle.right(angle) 
    turtle.end_fill()   

    
for i in range(10000):
    draw_A_Polygon(random.randint(3,11), random.randint(50,100))
    
turtle.done()