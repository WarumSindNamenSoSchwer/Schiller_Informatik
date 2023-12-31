import turtle as t
import time


#t.setup(1.0, 1.0)
screen = t.Screen()

def Hangmandraw(leben):

    t.speed(1)
    t.pensize(10)
    t.ht()

    #Galgen Basis
    if leben == 10:
        t.penup()
        t.right(90)
        t.forward(100)
        t.left(90)
        t.pendown()
        t.forward(100)

    if leben == 9:
        #Galgen Stange
        t.backward(50)
        t.left(90)
        t.forward(300)

    if leben == 8:
        #Galgen Horizontal Strich
        t.right(90)
        t.forward(125)

    if leben == 7:
        #Querbalken
        t.backward(125)
        t.right(90)
        t.forward(50)
        t.goto(125, 200)

    if leben == 6:
        #Seil
        t.left(90)
        t.forward(50)
        t.right(90)
        t.forward(25)
        t.forward(20)
        t.right(90)

    if leben == 5:
        #Kopf
        t.circle(20)
        t.penup()
        t.left(90)
        t.forward(40)

    if leben == 4:
        #torso
        t.pendown()
        t.forward(100)

    if leben == 3:
        #Arme
        t.backward(70)
        t.left(90)
        t.forward(25)
        t.backward(50)
        t.forward(25)
        t.right(90)
        t.forward(70)

    if leben == 2:
        #Bein 1
        t.right(45)
        t.forward(50)

    if leben == 1:
        #Bein 2
        t.backward(50)
        t.left(90)
        t.forward(50)
    

def easteregg():

    screen.bgpic("Hangman/Jynxzi.png")

    #easteregg
    t.clear()
    t.penup()
    t.home()
    t.reset()
    t.left(180)
    t.speed(0)
    t.pensize(10)
    t.ht()

    #kopf
    t.circle(20)
    t.penup()
    t.left(90)
    t.forward(40)

    #torso
    t.pendown()
    t.forward(100)

    #Arme
    t.backward(70)
    t.left(90)
    t.forward(25)
    t.backward(50)
    t.forward(25)
    t.right(90)
    t.forward(70)

    #Bein 1
    t.right(45)
    t.forward(50)

    #Bein 2
    t.backward(50)
    t.left(90)
    t.forward(50)

    time.sleep(2)

    t.clear()
    t.reset()

    screen.clear()

