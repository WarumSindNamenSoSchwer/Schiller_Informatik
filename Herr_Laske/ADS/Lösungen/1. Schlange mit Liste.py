class Schlange:
    def __init__(self):
        self.schlange = []

    # Ueberprueft ob die Schlange leer ist
    def istLeer(self):
        if len (self.schlange) == 0:
            return "Die Schlange ist leer!"
        else:
            return "Die Schlange ist nicht leer!"

    # Fuegt ein Element am Ende der Schlange ein
    def einreihen(self, wert):
        self.schlange.append(wert)


    # liefert den Kopf der Schlange, insofern die Schlange nicht leer ist
    def kopf(self):
        # falls die Schlange leer ist, Rückmeldung dazu
        if len (self.schlange) == 0:
            return "Die Schlange ist leer!"
        # sonst Lieferung des Kopfes der Schlange
        else:
            return self.schlange[0]

    # entfernt das erste Element der Schlange, insofern diese nicht leer ist
    def bedienen(self):
        if len (self.schlange) == 0:
            return "Die Schlange ist leer!"
        else:
            self.schlange.pop(0)

    # Gibt die Länge der Schlange zurück
    def laenge(self):
       return len (self.schlange)


    # Helfer um die Schlange auszugeben
    def __str__(self):
        beschreibung = str(self.schlange)
        return beschreibung
        
        
if __name__ == '__main__':
    liste = Schlange()
    print (liste)
    
    print ("Erzeugung einer neuen Schlange:")
    print ("Das ist die leere Schlange: ", liste)
    print ("Test von istLeer(): ", liste.istLeer())
    print ("Test von Einreihen (1-2-3):")
    liste.einreihen(1)
    print (liste)
    liste.einreihen(2)
    print (liste)
    liste.einreihen(3)
    print (liste)
    print()
    print ("Teste von länge(): ")
    print ("Länge der Schlange: ", liste.laenge())
    print()
    print ("Test von istLeer(): ", liste.istLeer())
    print ("Test von kopf(): ", liste.kopf())
    print()
    print ("Test von bedienen(): ")
    print ("aktuelle Schlange: ", liste)
    print ()
    for i in range (3):
        liste.bedienen()
        print ("aktuelle Schlange: ", liste)
        print ("Test von kopf(): ", liste.kopf())
        print ("aktuelle Länge: ", liste.laenge())

    

    

