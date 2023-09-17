'''
Autor: Murat
Thema: Einführung in Funktionen
Datum: 17.09.23
'''

'''
Zu erst einmal, was sind Funktionen und wo haben wir diese, vielleicht schon gesehen?

Funktionen sind wiederverwendbare Code-Blöcke die eine spefzifische Aufgabe ausführen
und sogennante Parameter akzeptieren.

 ->     funktion(Parameter1, Parameter2, ParameterN):
            Code
'''

'''
Eine Funktion die wir sehr gut kennen ist die "print" funktion.
'''
print("ich bin eine Funktion!")

'''
In Python sind Funktionen volgendermaßen struckturiert:
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
Immer wenn wir diese Funktion nun aufrufen/callen wird der Code in dieser ausgeführt.
'''

myFunc()
# Ausgabe -> Meine erste Funktion!

