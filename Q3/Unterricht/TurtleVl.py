'''
Zu erst was ist die Turtle-library.

Die Turtle-library ist eine Möglichkeit, einfache Grafiken zu zeichnen.
Mit ihr kann man eine virtuelle Schildkröte steuern, die auf einem Zeichenfenster, 
Zeichnungen erstellt.

1.	Turtle initialisieren: Zuerst muss man die turtle-Library importieren und 
eine Turtle erstellen, die man dann steuern kann.
'''

import turtle as t
# Oder
import turtle
t = turtle.Turtle()
# Oder
from turtle import *

'''
In der ersten Methode wird die Turtle-library importiert und ihr der Alias t gegeben
das ermöglicht es auf alle Funktionen und Objekte der Turtle-library über den Alias
zuzugreifen.

In der zweiten Methode wird wieder T. importiert aber diesmal erstellt man eine 
Schildkröte mit dem Namen t. In diesem fall kann man über t auf alle Funktionen und 
Methoden der Schildkröte zugreifen.

Beide Methoden sind richtig und gleich es ist Präferenz, wie immer gilt: 
-Benutzt das was für euch leichter zu verstehen und vorallem leserlicher ist.

In der dritten Methode werden alle funktionen und methoden im aktuellen Namensraum
importiert, was bedeutet ,dass wir sie dierekt aufrufen können ohne 
"t" oder "turtle" davor schreiben zu müssen.

2.	Bewegungsfunktionen: Die Schildkröte kann sich vorwärts oder rückwärts bewegen und 
sich drehen.
'''

t.forward(distanz) #Bewegt die Schildkröte um die angegebene Entfernung vorwärts.
t.backward(distanz) #Bewegt die Schildkröte um die angegebene Entfernung rückwärts.
t.left(winkel) #Dreht die Schildkröte um den angegebenen Winkel nach links.
t.right(winkel) #Dreht die Schildkröte um den angegebenen Winkel nach rechts.


'''
3.	Stiftfunktionen: Die Schildkröte kann einen Stift haben, den sie auf das Zeichenfenster 
drückt, um Linien zu zeichnen.
'''

t.penup() #Hebt den Stift, damit die Schildkröte sich bewegen kann, ohne Linien zu zeichnen.
t.pendown() #Senkt den Stift, um Linien zu zeichnen, wenn sich die Schildkröte bewegt.


'''
4.	Farb- und Füllfunktionen: Du kannst die Farbe des Stifts und des Hintergrunds ändern und 
Bereiche mit Farbe füllen.
'''

t.pencolor(farbe) #Ändert die Farbe des Stifts.
t.fillcolor(farbe) #Ändert die Füllfarbe für Formen, die du zeichnen möchtest.
t.begin_fill() #Beginnt mit dem Füllen einer Form.
t.end_fill() #Beendet das Füllen einer Form.


'''
5.	Rückkehr zur Startposition + Postitionsänderung: Du kannst die Schildkröte zur 
Startposition zurückkehren lassen oder die Schildkröte auf eine bestimmte Koordinate im 
Zeichenfenster setzen
'''

t.home() #Bringt die Schildkröte zur Startposition zurück (0, 0).
t.goto(x,y) #Setz die Schildkröte an eine bestimmte Koordinate: x = Horizontal, y = Vertikal

'''
6.	Zeichenfenster: Du kannst das Zeichenfenster steuern.
'''

turtle.done() #Beendet das Zeichenfenster, wenn du fertig bist.


'''
Aufgaben:

Aufgabe 1: Zeichne ein Quadrat mit der Schildkröte.

Aufgabe 2: Zeichne ein gleichseitiges Dreieck.

Aufgabe 3: Zeichne ein Rechteck mit unterschiedlichen Farben für den Rand und die Füllung.

Aufgabe 4: Zeichne ein Haus mit Fenstern und einer Tür.
'''


