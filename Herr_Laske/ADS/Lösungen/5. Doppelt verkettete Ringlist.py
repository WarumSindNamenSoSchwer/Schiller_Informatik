#doppelt-verkettete Ringliste mit Anker-Element

class Knoten: 
    # zum Initialisieren
    def __init__(self,inhalt): 
        self.inhalt = inhalt 
        # Zeiger auf das naechste und das vorherige Element der Liste
        self.naechster = None
        self.vorheriger = None


class Schlange:
    def __init__(self):
        #Ankerelement wird erstellt:
        k = Knoten('XankerX')
        k.naechster= k
        k.vorheriger=k
        self.anker=k
        
        self.aktuellesElement=k #Ankerelement ist am Anfang auch das aktuelle Element:
        self.aktuellerIndex = 0
        self.länge = 0

    # Vor.: -
    # Erg:Liefert True, wenn die Folge/Schlange leer ist, andernfalls False.
    def istLeer(self):
        return self.anker.naechster == self.anker and self.anker.vorheriger == self.anker

    # Vor.: -
    # Eff.: Das gegebene Element ist vor dem aktuellen Element eingefügt.
    def Einfügen(self,wert):
        k = Knoten(wert)
        k.naechster = self.aktuellesElement
        k.vorheriger = self.aktuellesElement.vorheriger
        self.aktuellesElement.vorheriger.naechster = k
        self.aktuellesElement.vorheriger = k
        if self.aktuellesElement == self.anker:
            self.aktuellerIndex = 0
        else:
            self.aktuellerIndex += 1
        self.länge += 1
        

    # Vor.: -
    # Eff.: Gab es ein Element mit Index n in der Folge, so ist es nun
    #       aktuelles Element. Andernfalls ist kein Element aktuell.
    def Positionieren(self,n):
        if n < self.länge:
            self.aktuellerIndex = n 
            self.aktuellesElement = self.anker
            for i in range(self.aktuellerIndex): 
                self.aktuellesElement = self.aktuellesElement.naechster
        else:
            self.aktuellesElement = self.anker
            self.aktuellerIndex = 0
        
        

    # Vor.: -
    # Erg.: War die Folge leer oder gab es kein aktuelles Element, so 
    #       ist die Länge der Folge geliefert, andernfalls ist der
    #       (Positions-)Index des aktuellen Elements geliefert. 
    def AktuellerIndex(self):
    	if self.istLeer():
    		return self.Länge()
    	else:	
    		return self.aktuellerIndex

    # Vor.: -   
    # Erg.: Falls es kein aktuelles Element gab, wird dies so zurückgegeben.
    #       Ansonsten ist das aktuelle Element e geliefert.
    def AktuellesElement(self):
        if self.aktuellesElement == self.anker:
            return "Es gibt kein aktuelles Element! (= Anker)"
        else:
            e = self.aktuellesElement.inhalt
            return e

    # Vor.: -
    # Eff.: War kein Element aktuell so ist nichts passiert.                    
    #       Ansonsten ist das dem ehemals aktuellen Element folgende Element
    #       nun aktuell. Gibt es ein solches Element nicht, so ist kein 
    #       Element aktuell.
    def Vor(self):
        if self.aktuellerIndex == 0:
            return
        elif self.aktuellerIndex == self.länge:
            return
        else:
            self.aktuellesElement = self.aktuellesElement.naechster
            self.aktuellerIndex += 1
            
            

    # Vor.: -
    # Eff.: War das Element mit Index 1 aktuell, so ist nichts passiert.        #Also nicht 0, da unser erstes Element Index 1 hat. //Fehlerhaft, da wir ja bei 1 Starten wollen
    #       War kein Element aktuell, so ist nun das letzte Element aktuell.    
    #       Ansonsten ist das dem ehemals aktuellen Element vorhergehende
    #	    Element aktuell.
    def Zurück(self):
        if self.aktuellerIndex == 1:    #Je nachdem, ob man den Anker als Wand einschließt oder nicht. 0 oder 1, 1 würde bedeuten, der Anker ist außen vor.
            return
        else:
            self.aktuellesElement = self.aktuellesElement.vorheriger
            self.aktuellerIndex -= 1
            
            

    # Vor.: -
    # Eff.: Gab es ein aktuelles Element, so ist es aus der Liste
    #       entfernt, alle anderen Elemente bleiben in gleicher Reihenfolge.
    #       Das vorherige folgende Element ist jetzt aktuell. Gibt es ein 
    #       solches Element nicht, so ist kein Element aktuell.
    #       Gab es kein aktuelles Element, so ist nichts passiert.
    def Löschen(self):
        if self.aktuellesElement != self.anker:
            self.aktuellesElement.vorheriger.naechster = self.aktuellesElement.naechster
            self.aktuellesElement.naechster.vorheriger = self.aktuellesElement.vorheriger
            self.aktuellesElement = self.aktuellesElement.naechster
            if self.aktuellesElement == self.anker:
                self.aktuellerIndex = 0
            self.länge -= 1


    # Vor.: -
    # Erg.: Die Laenge der Folge, d. h. die Anzahl der Elemente
    #       in der Folge, ist geliefert.
    def Länge(self):
        return self.länge
        

    # Vor.: Der Kunde  hat eine Funktion def__str__() zur Verfügung gestellt,
    #       die zu einem Element einen darstellenden String liefert.
    # Erg.: Ein String ist geliefert, der die Schlange/Folge als Zeichenkette
    #       darstellt.
    def __str__(self):
        tmpptr = self.anker
        erg = "<:)-"
        while tmpptr.naechster != self.anker:
            tmpptr = tmpptr.naechster
            erg = erg + str(tmpptr.inhalt) + "-"
            
        erg = erg + "<<<  " + "  Länge: " + str(self.länge)

        erg = erg + "  aktueller Index: " + str(self.aktuellerIndex)
    
        erg = erg + "\n" + "Aktuelles Element: " + str(self.AktuellesElement())

        return erg
        

if __name__ == '__main__':
    liste = Schlange()
    print ("aktuelle Schlange: ", liste)
    print("Leer?: ", liste.istLeer())
    print ("Einfügen von a-b-c")
    liste.Einfügen('a')
    liste.Einfügen('b')
    liste.Einfügen('c')
    print ("aktuelle Schlange: ", liste)
    print()
    
    print ("Positionieren auf Index 1000 --> Diesen gibt es hier gar nicht, daher weiterhin normales Einfügen am Schluss:")
    liste.Positionieren(1000)
    print ("Einfügen eines 'd':")
    liste.Einfügen("d")
    print ("aktuelle Schlange: ", liste)
    print()
    
    print ("Positionieren auf das 3. Element ('c'):")
    liste.Positionieren(3)
    print("Aktuelles Element: ", liste.AktuellesElement())
    print("Aktueller Index: ", liste.AktuellerIndex())
    print ("Einfügen einer '1':")
    liste.Einfügen("1")
    print ("aktuelle Schlange: ", liste)
    print()
    
    print ("Positionieren auf das 1. Element ('a'):")
    liste.Positionieren(1)
    print ("Einfügen eines 'A':")
    liste.Einfügen("A")
    print ("aktuelle Schlange: ", liste)

    print()
    print ("Test von 'Zurück', aktuelles Element ist immer noch 'a', entspricht 2. Stelle")
    liste.Zurück()
    print ("aktuelle Schlange: ", liste)
        
    print()
    print ("Test von 'Vor', aktuelles Element ist 'A' = 1. Element der Liste:")
    for i in range (5):
        liste.Vor()
        print ("aktuelle Schlange: ", liste)

    print()
    print ("Test von 'Vor', aktuelles Element ist das letzte Element, es dürfte nichts passieren:")
    liste.Vor()
    print ("aktuelle Schlange: ", liste)

    print()
    print ("Test von 'Zurück', aktuelles Element ist das letzte, das vorletzte Element müsste aktuell werden:")
    liste.Zurück()
    print ("aktuelle Schlange: ", liste)

    print()
    print("Testen von Löschen, sprich das 'c' wird gelöscht, das neue aktuelle Element wird 'd': ")
    liste.Löschen()
    print ("aktuelle Schlange: ", liste)

    print()
    print("Testen von Löschen ('d'), wenn der Anker das nächste Element ist. Sprich, der Anker müsste das neue 'aktuelle Element' werden.")
    liste.Löschen()
    print ("aktuelle Schlange: ", liste)

    print()
    print("Nochmaliges Testen von Löschen, nach Positionierung auf 1. Indexstelle ('A'): ")
    liste.Positionieren(1)
    liste.Löschen()
    print ("aktuelle Schlange: ", liste)

    print ()
    print("Testen von Einfügen ('Z') an Position 2, also vor dem aktuell zweiten Element ('b')")
    liste.Positionieren(2)
    liste.Einfügen("Z")
    print ("aktuelle Schlange: ", liste)

    print()
    print("Positionieren auf Index 100 (gibt es nicht), Anker müsste wieder 'aktuelles Element werden'.")
    liste.Positionieren(100)
    print("Aktueller Index: ", liste.AktuellerIndex())

    print()
    print("Letzter Einfügetest ('X'), das Element müsste an der letzten Stelle einfegügt werden.")
    liste.Einfügen("X")
    print ("aktuelle Schlange: ", liste)


    
    

    
    
        
    
    

  


