'''
Autor: Murat
Thema: Einführung in Funktionen
Datum: 17.09.23
'''

'''
Zu erst einmal, was sind Funktionen und wo haben wir diese vielleicht schon gesehen?

Funktionen sind wiederverwendbare Code-Blöcke die eine spezifische Aufgabe ausführen
und sogennante Parameter Akzeptieren.

->    funktion(Parameter1, Parameter2, ParameterN):
        Code
'''

'''
Eine Funktion die wir sehr gut kennen ist die "print" funktion.
'''
print("Ich bin eine Funktion!")

'''
In Python sind Funktionen folgendermaßen Strukturiert:
    - Erst kommt der Name der Funktion, hier z.B. "print"
    - Dann kommen die Klammern, in denen befinden sich dann die Parameter.
      Eine Funktion muss nicht immer Parameter haben.
    - Wie wir wissen können wir Strings, Zahlen und Variablen als Parameter übergeben.
      Diese Parameter werden Speziell "objects" genannt.
    - "print" kann aber auch Listen, Tupel, Dictionaries und Boolesche Werte als "objects" erhalten.

Um nun eine eigene Funktion zu erstellen braucht man das Schlüsselwort "def" (-> Define)
'''
def myFunc():
    print("Meine erste Funktion!")

'''
Immer wenn wir diese Funktion nun aufrufen (-> diese Aktion nennt man function call) 
wierd der Code in dieser ausgeführt.
'''
myFunc()
# Ausgabe -> Meine erste Funktion!

'''
Aufgabe 1: Erstelle eine Funktion die zwei Zahlen addiert, die Zahlen sollen als Parameter
übergeben werden.

Aufgabe 2: Erstelle eine Begrüßungsfunktion die den Namen als Parameter nimmt und den Nutzer Anschließend 
begrüßt.

Aufgabe 3: Erstelle eine Funktion die, die Summe einer Zahlenreihe von 1 bis zu einer 
Zahl, die als Parameter übergeben wurde errechnet.

Aufgabe 4: Erstelle eine Funktion, die die Länge einer Zeichenkette (String) zählt und die Anzahl der 
Zeichen zurückgibt. Zum Beispiel sollte die Eingabe “Hallo” die Ausgabe 5 liefern.
'''


