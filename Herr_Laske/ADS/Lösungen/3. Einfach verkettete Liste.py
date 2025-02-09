class Knoten:
    def __init__(self):
        self.inhalt = None
        self.naechster = None

    #def __str__(self):
     #   return str(self.inhalt)
        

class Schlange:
    def __init__(self):
        self.laenge = 0
        self.kopfzeiger = None
        self.endzeiger = None

    # Ueberprueft ob die Schlange leer ist
    def istLeer(self):
        if self.laenge == 0:
            return "Die Schlange ist leer!"
        else:
            return "Die Schlange ist nicht leer!"

    # Fuegt ein Element am Ende der Schlange ein
    def Einreihen(self, wert):
        knoten = Knoten()
        knoten.inhalt = wert
        knoten.naechster = None
        if self.laenge == 0: #leer Schlange
            self.kopfzeiger = knoten
            self.endzeiger = knoten
            self.laenge += 1
        else:
            self.endzeiger.naechster = knoten
            self.endzeiger = knoten
            self.laenge += 1


    # liefert den Kopf der Schlange, insofern die Schlange nicht leer ist
    def Kopf(self):
        # falls die Schlange leer ist, Rückmeldung dazu
        if self.laenge == 0:
            return "Die Schlange ist leer!"
        # sonst Lieferung des Kopfes der Schlange
        else:
            return self.kopfzeiger.inhalt

    # entfernt das erste Element der Schlange, insofern diese nicht leer ist
    def Bedienen(self):
        if self.laenge == 0:
            return "Die Schlange ist leer!"
        else:
            self.kopfzeiger = self.kopfzeiger.naechster
            self.laenge -= 1
            if self.laenge == 0:
                self.endzeiger = None
                self.kopfzeiger = None

    # Gibt die Länge der Schlange zurück
    def Laenge(self):
       return self.laenge


    # Helfer um die Schlange auszugeben
    def __str__(self):
        erg = ""
        pointer = self.kopfzeiger
        if pointer == None:
            return "[ ]"
        else:
            erg = erg + "[<:)- "
            while pointer != None:
                erg = erg +  str(pointer.inhalt) + " <-- " 
                pointer = pointer.naechster
            erg = erg + "<]"
            return erg
        
        
        
if __name__ == '__main__':
    liste = Schlange()

    print ("Erzeugung einer neuen Schlange:")
    print ("Das ist die leere Schlange: ", liste)
    print ("Test von istLeer(): ", liste.istLeer())
    print ("Test von Einreihen (1-2-3):")
    liste.Einreihen(1)
    print (liste)
    liste.Einreihen(2)
    print (liste)
    liste.Einreihen(3)
    print (liste)
    print ("Teste von Länge: ")
    print ("Länge der Schlange: ", liste.Laenge())
    print ("Test von istLeer(): ", liste.istLeer())
    print ("Test von Kopf(): ", liste.Kopf())
    print ("Test von Bedienen(): ")
    liste.Bedienen()
    print ("aktuelle Schlange: ", liste)
    print ("aktuelle Länge: ", liste.Laenge())
    print ("Test von Einreihen (77):")
    liste.Einreihen(77)
    print ("aktuelle Schlange: ", liste)
    print ("aktuelle Länge: ", liste.Laenge())

    

    

