from turtle import Screen, Turtle
import random as r

screen = Screen() # Erstellt das Screen-Objekt
screen.setup(width=800, height=600) # Setzt die Groesse des Screens
screen.bgpic('T_Rennen/bg/road.gif') # Setzt den Hintergrund

yPosition = [-260, -172, -85, 2, 85, 172, 260] # Liste mit y-Positionen
tFarbe = ['red', 'green', 'yellow', 'blue', 'purple', 'pink', 'orange'] # Liste mit Farben
alleTurtles = [] # Leere Liste fuer alle Turtles

for index in range(7): # Schleife fuer 7 Turtles
    t = Turtle(shape='turtle') # Erstellt Turtle
    t.speed(0) # Setzt Geschwindigkeit
    t.penup() # Hebt Stift hoch
    t.shapesize(3) # Setzt Groesse
    t.color(tFarbe[index]) # Setzt Farbe
    t.goto(x=-360, y= yPosition[index]) # Setzt Startposition
    alleTurtles.append(t) # Fuegt Turtle zur Liste hinzu

istAn = True # Variable um Schleife zu steuern
SCHRIFT = ("Courier", 16, "bold") # Schriftart fuer Text
AUSRICHTUNG = "right" # Ausrichtung fuer Text

wette = screen.textinput('Turtlewette', 'Auf welche Turtle wettest du? (Farbe in Englisch)', ).lower() # Fragt nach Wette

while istAn: # Hauptschleife
    for t in alleTurtles: # Schleife ueber alle Turtles
        if t.xcor() > 340: # Wenn Turtle im Ziel
            istAn = False # Schleife beenden
            gewinner = t.pencolor() # Farbe des Gewinners
            if gewinner == wette: # Vergleich mit Wette
                t.write(f'Du hattest recht! {gewinner} hat gewonnen.',font=SCHRIFT, align=AUSRICHTUNG) # Ausgabe bei richtiger Wette
            else:
                t.write(f'Schade, {gewinner} hat gewonnen.',font=SCHRIFT, align=AUSRICHTUNG) # Ausgabe bei falscher Wette
        zufallsGeschwindigkeit = r.randint(0, 15) # Zufallsgeschwindigkeit
        t.forward(zufallsGeschwindigkeit) # Bewegt Turtle

screen.exitonclick() # Beendet Programm bei Klick
