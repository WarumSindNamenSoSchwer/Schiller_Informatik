class Knoten():
    def __init__(self):
        self.inhalt = None
        self.naechster = None

class Schlange():
    def __init__(self):
        self.laenge = 0
        self.endzeiger = None

    def IstLeer(self):
        return self.laenge == 0

    def Einreihen(self,wert):
        knoten = Knoten()                       #1. Neuer Knoten wird erstellt
        knoten.inhalt = wert                    #2. Dem neuen Knoten wird ein Inhalt gegeben

        if self.IstLeer():                      #3. Es wird geprüft, ob die Schlange leer ist.
            self.endzeiger = knoten             #4. Der aktuelle Endzeiger wird auf den Knoten gebogen
            self.endzeiger.naechster = knoten   #5. Der Verweis "nächster" des Endzeigers wird auf den Knoten gebogen (zeigt also in diesem Fall auf sich selbst).

        else:                                   #3. Wenn die Schlange nicht leer ist.
            
            knoten.naechster = self.endzeiger.naechster #4. Der Verweis "nächster" des neuen Knotens wird auf das nächste Element des Enzeigers gebogen.
            self.endzeiger.naechster = knoten           #5. Der Verweis "nächster" des Endzeigers wird auf den Knoten gebogen.
            self.endzeiger = knoten                     #6. Der Endzeiger wird auf den neuen Knoten gerichtet, da dieser das neue letzte Element in der Schlange ist.
        self.laenge += 1                                #7. Die Länge der Schlange wird um 1 erhöht.


    def Kopf(self):
        if self.IstLeer():
            return "Die Schlange ist leer!"
        else:
            return self.endzeiger.naechster.inhalt # Der Inhalt des Kopfelements der Schlange wird über den Verweis "nächster" des Endzeigers erreicht.

    def Bedienen(self):
        if self.IstLeer():
            return "Die Schlange ist leer!"
        else:
            self.endzeiger.naechster = self.endzeiger.naechster.naechster # Da man den Kopf der Schlange über den Verweis "nächster" des Endzeigers erreicht, 
            self.laenge -= 1                                              # muss dieser Verweis aufgehoben und um ein Elemte nach vorne gesetzt werden.
                                                                          # Zudem wird die Länge um eins verringert.
        
    def Laenge(self):
        return self.laenge


    def __str__(self):
        erg = "<:)- "
        if self.IstLeer():
            return "[ ]"
        else:
            ringpointer = self.endzeiger.naechster              # Es ist notwendig mit einem temporären Zeiger (Kopie) über die Schlange zu laufen, da sonst die Datenstruktur zerstört wird.
            for i in range(self.laenge):
                erg = erg + str(ringpointer.inhalt) + " - "
                ringpointer = ringpointer.naechster
            erg = erg + "<<"
        return erg

#Test

if __name__ == '__main__':
    liste = Schlange()

    print ("Erzeugung einer neuen Schlange:")
    print ("Das ist die leere Schlange: ", liste)
    print ("Test von istLeer(): ", liste.IstLeer())
    print ("Test von Einreihen (1-2-3):")
    liste.Einreihen(1)
    print (liste)
    liste.Einreihen(2)
    print (liste)
    liste.Einreihen(3)
    print (liste)
    print ("Länge der Schlange: ", liste.Laenge())
    print ("Test von istLeer(): ", liste.IstLeer())
    print ("Test von Kopf(): ", liste.Kopf())
    print ("Test von Bedienen(): ")
    liste.Bedienen()
    print ("aktuelle Schlange: ", liste)
    print ("aktuelle Länge: ", liste.Laenge())
    print ("Test von Einreihen (77):")
    liste.Einreihen(77)
    print ("aktuelle Schlange: ", liste)
    print ("aktuelle Länge: ", liste.Laenge())
    print(liste)
    print("Schlange leeren: ")
    for i in range(3):
        liste.Bedienen()
    print ("aktuelle Schlange: ", liste)
    print ("aktuelle Länge: ", liste.Laenge())
    print ("Test von istLeer(): ", liste.IstLeer())
    


        
