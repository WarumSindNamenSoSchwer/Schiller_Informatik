from turtle import Screen, Turtle
import random as r

screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic('T_Rennen/bg/road.gif')

yPosition = [-260, -172, -85, 2, 85, 172, 260]
tFarbe = ['red', 'green', 'yellow', 'blue', 'purple', 'pink', 'orange']
alleTurtles = []

for index in range(7):
    t = Turtle(shape='turtle')
    t.speed(0)
    t.penup()
    t.shapesize(3)
    t.color(tFarbe[index])
    t.goto(x=-360, y= yPosition[index])
    alleTurtles.append(t)

istAn = True
SCHRIFT = ("Courier", 16, "bold")
AUSRICHTUNG = "right"

wette = screen.textinput('Turtlewette', 'Auf welche Turtle wettest du? (Farbe in Englisch)', ).lower()

while istAn:
    for t in alleTurtles:
        if t.xcor() > 340:
            istAn = False
            gewinner = t.pencolor()
            if gewinner == wette:
                t.write(f'Du hattest recht! {gewinner} hat gewonnen.',font=SCHRIFT, align=AUSRICHTUNG)
            else:
                t.write(f'Schade, {gewinner} hat gewonnen.',font=SCHRIFT, align=AUSRICHTUNG)
        zufallsGeschwindigkeit = r.randint(0, 15)
        t.forward(zufallsGeschwindigkeit)

screen.exitonclick()