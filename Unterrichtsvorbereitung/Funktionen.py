'''
Autor: Murat
Thema: Einführung in Funktionen
Datum: 17.09.23
'''

'''
Zu erst einmal, was sind Funktionen und wo haben wir diese vielleicht schon gesehen?

Funktionen sind wiederverwendbare Code-Blöcke die eine spezifische Aufgabe ausführen
und sogennante Parameter akzeptieren.

 ->     funktion(Parameter1, Parameter2, ParameterN):
            Code
'''

'''
Eine Funktion die wir sehr gut kennen ist die "print" funktion.
'''
print("ich bin eine Funktion!")

'''
In Python sind Funktionen folgendermaßen strukturiert:
       - Erst kommt der Name der Funktion, hier z.B. "print"
       - Dann kommen die Klammern, in denen befinden sich dann die Parameter.
         Eine Funktion muss nicht immer Parameter haben.
       - Wie wir wissen können wir Strings, Zahlen und Variablen als Parameter übergeben.
         Diese Parameter werden Speziell "objects" genannt.
       - "print" kann aber auch Listen, Tupel, Dictionaries, Boolesche Werte, Funktionen
         und Klassen und deren Objekte als "objects" erhalten.


Um nun eine Eigene Funktion zu erstellen braucht man das Schlüsselwort "def"
'''
def myFunc():
    print("Meine erste Funktion!")

'''
Immer wenn wir diese Funktion nun aufrufen (-> wird function call genannt) wird
der Code in dieser ausgeführt.
'''
myFunc()
# Ausgabe -> Meine erste Funktion!

'''
Aufgabe 1: Schreib eine Funktion die zwei Zahlen addiert, die Zahlen sollen als Parameter
übergeben werden.

Aufgabe 2: Schreib eine Begrüßungsfunktion die den Namen als Parameter nimmt und diese 
begrüßt.

Aufgabe 3: Schreib eine Funktion die, die Summe einer Zahlenreihe von 1 bis zu einer 
Zahl, die als Parameter übergeben wurde errechnet.
'''

#----------------------------------------------------------------------------------------------

'''
Turtle
'''

'''
Zu erst muss die Library für turtle importiert werden, da man sonst die Funktionen der Library nicht benutzen kann.

Das macht man mit dem Schlüsselwort : import
'''

import turtle

pen = turtle.Turtle()

def curve():
  for i in range(200):
    pen.right(1)
    pen.forward(1)

def fig():
  pen.fillcolor('crimson')
  pen.begin_fill()
  pen.left(140)
  pen.forward(113)
  curve()
  pen.left(120)
  curve()
  pen.forward(112)
  pen.end_fill()

fig()

turtle.done()
pen.ht()

turtle.bgcolor('black')
t = turtle.Turtle()
colors = ['red', 'dark red']
for numbers in range(400):
  t.forward(numbers+1)
  t.right(89)
  t.pencolor(colors[numbers%2])
    