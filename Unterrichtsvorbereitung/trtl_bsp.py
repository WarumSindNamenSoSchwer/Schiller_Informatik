#'''

import turtle
t = turtle.Turtle()
screen = turtle.Screen()
screen.screensize(canvheight=1000, canvwidth=1000)

t.speed(0)
t.pensize(4)
t.color("black")
size_of_graphic = 200

def circular_band():
    t.begin_fill()
    t.circle(size_of_graphic) 
    t.end_fill()
    t.goto((22 / 24) * size_of_graphic, 0)
    t.fillcolor("yellow")
    t.begin_fill()                          
    t.circle((22 / 24) * size_of_graphic)
    t.end_fill()

def three_rays():
    t.color("black")
    t.begin_fill()
    for i in range(3):
        t.forward((40 / 24) * size_of_graphic)
        t.left(90)
        t.circle((20 / 24) * size_of_graphic, 60)
        t.left(90)
    t.end_fill()

def center():
    t.color("yellow")
    t.begin_fill()                              
    t.circle((6 / 24) * size_of_graphic)
    t.end_fill()
    t.goto((4 / 24) * size_of_graphic, 0)
    t.color("black")
    t.begin_fill()                      
    t.circle((4 / 24) * size_of_graphic)
    t.end_fill()

t.penup()
t.goto(size_of_graphic, 0)
t.left(90)
t.pendown()
circular_band()
t.penup()
t.goto((-20 / 24 * size_of_graphic), 0)
t.right(90)
t.pendown()
three_rays()
t.penup()
t.home()
t.forward((6 / 24) * size_of_graphic)
t.left(90)
t.pendown()
center()
t.hideturtle()

screen.exitonclick()

#'''

'''
#oder:
import turtle as t 

t.bgcolor('black')
t.color('yellow')
t.write('☢', align="center", font=("ariel", 200))
t.ht()

screen.exitonclick()
'''