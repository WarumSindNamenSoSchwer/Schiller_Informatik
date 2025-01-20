#Autor: Annisa Kapur und Murat-Can Meric
#Datum: 06.01.2024
#Thema: doppelt verkettete Ringliste


"""
Aufgaben:
1.  Zeichnen Sie das Einfügen eines Knotens k in eine leere Liste (mit Schriftfolge).
2.  Zeichnen Sie das Einfügen eines Knotens k in eine nicht leere Liste (mit Schriftfolge).
3.  Zeichnen Sie den Löschvorgang eines Knotens k in einer nicht leeren Liste (mit Schrittfolge).  
4.  Implementieren Sie die vorliegende Spezifikation unter Berücksichtigung der jeweiligen Voraussetzungen und Effekte/Ergebnisse in Python. 

Schreiben Sie eine Python-Klasse zur Verwaltung einer doppelt verketteten Ringliste mit einem Anker-Element.
Nutzen Sie die folgende Dokumentation als Hilfe.
Ziel ist es, die Funktionsweise solcher Listen zu verstehen und eine eigene Implementierung zu entwickeln.


Hintergrund:

Eine doppelt verkettete Ringliste ist eine Datenstruktur, bei der jeder Knoten auf den nächsten und den vorherigen Knoten verweist.
Der letzte Knoten ist mit dem ersten verbunden,wodurch eine Ringstruktur entsteht. Zusätzlich gibt es ein Anker-Element, das nicht
als Datenknoten zählt, sondern den Startpunkt der Liste definiert.
"""

class Node:
    """
    Klasse, die einen einzelnen Knoten in der doppelt verketteten Ringliste darstellt.
    """
    def __init__(self, data):
        """
        Initialisiert einen Knoten mit einem gegebenen Inhalt.
        Parameterinhalt: beliebiger Inhalt des Knotens.
        """
        self.data = data
        self.next = None
        self.prev = None
        

class Buffer:
    """
    Klasse, die eine doppelt verkettete Ringliste mit einem Anker-Element verwaltet.
    """
    def __init__(self):
        """
        Initialisiert die Ringliste mit einem Anker-Element.
        """
        self.länge = 0  # Länge 0-initialisieren
        self.sentinel= Node(data = "ANKER")   # Anker-Element mit Inhalt erstellen 
        self.sentinel.prev = self.sentinel   # Der Anker zeigt auf sich selbst (vorheriger Knoten)
        self.sentinel.next = self.sentinel   # Der Anker zeigt auf sich selbst (nächster Knoten)

        self.current_element = self.sentinel # Anker-Element ist initial das aktuelle Element
        self.current_index = 0   # Index 0 setzen, da 1-basierter Index  
        

    def istLeer(self)-> bool:
        """
        Überprüft, ob die Ringliste leer ist.
        :return: True, wenn die Liste leer ist, ansonsten False.
        """
        return self.länge == 0

    def Einfügen(self, wert):
        """
        Fügt ein neues Element vor dem aktuellen Element ein.
        Parameterwert: Der Inhalt des neuen Knotens.
        """
        node = Node(wert) #1
        node.next = self.current_element #2
        node.prev = self.current_element.prev #3
        self.current_element.prev.next = node #4
        self.current_element.prev = node #5
        self.current_element = node # 5.5
        self.länge += 1 #6
        if  self.sentinel != self.current_element: #selbe wie nicht leer
            self.current_index += 1 #7
        

    def Positionieren(self, n):
        """
        Positioniert das aktuelle Element auf das Element mit dem Index n (1-basiert).
        Paramenter n: Der Index des gewünschten Elements (1-basiert).
        """
        if n < 1 or n > self.länge: #Bedningunge für n  
            print("Ungültige Position. Die Länge des Puffers ist {self.länge}")
        else:
            self.current_element = self.sentinel #bei anker anfangen 
            for _ in range (n-1) :
                self.current_element = self.current_element.next  #next bis auf n.Index verschieben
            self.current_index = n
        #(self.sentinel.prev.data )
        

    def AktuellerIndex(self):
        """
        Gibt den aktuellen Index zurück.
        return: Index des aktuellen Elements oder 0, wenn kein Element ausgewählt ist.
        """
        return self.current_index

    def AktuellesElement(self):
        """
        Gibt den Inhalt des aktuellen Elements zurück.
        return: Inhalt des aktuellen Elements oder eine Nachricht, wenn kein Element (der Anker) aktuell ist.
        """
        return self.current_element.data
    
    def Vor(self):
        """
        Verschiebt das aktuelle Element auf das nächste Element, insofern nicht der Anker das aktuelle Element ist.
        """
        if self.current_element != self.sentinel:
            self.current_element = self.current_element.next

    def Zurück(self):
        """
        Verschiebt das aktuelle Element auf das vorherige Element, insofern nicht der Anker das aktuelle Element ist.
        """
        if self.current_element != self.sentinel:
           self.current_element = self.current_element.prev

    def Löschen(self):
        """
        Entfernt das aktuelle Element aus der Liste. Das ehemals folgende Element des aktuellen Element ist nun das aktuelle Element.
        """
        if self.current_element != self.sentinel: #Fall leer? #1
            self.current_element.prev.next = self.current_element.next #2
            self.current_element.next.prev = self.current_element.prev #3
            self.current_element = self.current_element.next if self.current_element != self.sentinel else self.sentinel #neue aktuelle element #4
            self.länge -= 1 #5
            self.current_index -= 1
        else:
            print( "Der Puffer ist leer")

    def Länge(self):
        """
        Gibt die Anzahl der Elemente in der Liste (ohne Anker) zurück.
        :return: Anzahl der Knoten außer dem Anker.
        """
        return self.länge 
        #while m != self.sentinel

    def __str__(self):
        """
        Gibt die Liste als Zeichenkette aus.
        """
        ergebnis = ""
        knoten = self.sentinel.next
        while knoten != self.sentinel:
            ergebnis += str(knoten.data)
            knoten = knoten.next
        if knoten == self.sentinel.next:
            return "ANKER <-> ANKER"
        return " <-> ".join(ergebnis)

# Testprogramm
if __name__ == '__main__':
    
    """
    Testen Sie Ihre Klasse mit mindestens drei Elementen (a, b, c)
    und überprüfen Sie alle Methoden.

    Beispieltest:

    Einfügen von Elementen.

    Positionieren auf ein bestimmtes Element.

    Bewegen des aktuellen Elements vor und zurück.

    Löschen von Elementen.
    """

    r = Buffer()
    print(str(r))
    print("Länge: " + str(r.Länge()))
    print("Leer? " + str(r.istLeer()))
    print("Aktueller Index: " + str(r.AktuellerIndex()))
    print("Aktuelles Element: " + str(r.AktuellesElement()))

    print("\n-----------------TEST EINREIHEN-----------------\n")

    for i in range(6):
        r.Einfügen(i)
        print("Eingereiht: " + str(r.AktuellesElement()))
        print(str(r))
        print("Länge: " + str(r.Länge()))
        print("Leer? " + str(r.istLeer()))
        print("Aktueller Index: " + str(r.AktuellerIndex()))
        print("Aktuelles Element: " + str(r.AktuellesElement()))
        #r.Positionieren()
        #print("Aktuelles Element vorverschoben")
        #print("Aktuelles Element: " + str(r.AktuellesElement()))
        print()
  
    
    print("\n-----------------TEST LÖSCHEN-----------------\n")
    for i in range(3): 
        print("Löscht: " + str(r.AktuellesElement()))
        print(str(r))
        r.Löschen()
        print(str(r))
        print("Länge: " + str(r.Länge()))
        print("Leer? " + str(r.istLeer()))
        print("Aktueller Index: " + str(r.AktuellerIndex()))
        print("Aktuelles Element: " + str(r.AktuellesElement()))
        print()

        
    print("\n-------------TEST ERNEUT EINREIHEN-------------\n")
    for i in range(6,9):
        print("Eingereiht: " + str(r.Einfügen(i)))
        print(str(r))
        print("Länge: " + str(r.Länge()))
        print("Leer? " + str(r.istLeer()))
        print("Aktueller Index: " + str(r.AktuellerIndex()))
        print("Aktuelles Element: " + str(r.AktuellesElement()))
        print()

    print("\n-------------TEST POSITIONIEREN-------------\n")
    n = 6 
    print(f"Positionieren: {n}")
    r.Positionieren(n)
    #print("Aktuelles Element: " + str(r.AktuellesElement()))
    print("Aktueller Index: " + str(r.AktuellerIndex()))

   
