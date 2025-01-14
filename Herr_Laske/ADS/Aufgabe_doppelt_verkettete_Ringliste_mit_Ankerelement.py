class Knoten:
    """
    Klasse, die einen einzelnen Knoten in der doppelt verketteten Ringliste darstellt.
    """
    def __init__(self, inhalt):
        self.inhalt = inhalt
        self.next = None
        self.prev = None


class Schlange:
    """
    Klasse, die eine doppelt verkettete Ringliste mit einem Anker-Element verwaltet.
    """
    def __init__(self):
        self.anker = Knoten(None)  # Anker-Element
        self.anker.next = self.anker
        self.anker.prev = self.anker
        self.aktueller_knoten = self.anker
        self.laenge = 0

    def istLeer(self):
        return self.laenge == 0

    def Einfügen(self, wert):
        neuer_knoten = Knoten(wert)
        neuer_knoten.next = self.aktueller_knoten
        neuer_knoten.prev = self.aktueller_knoten.prev
        self.aktueller_knoten.prev.next = neuer_knoten
        self.aktueller_knoten.prev = neuer_knoten
        self.aktueller_knoten = neuer_knoten
        self.laenge += 1

    def Positionieren(self, n):
        if n < 1 or n > self.laenge:
            return "Ungültige Position"
        self.aktueller_knoten = self.anker.next
        for _ in range(n - 1): 
            self.aktueller_knoten = self.aktueller_knoten.next

    def AktuellerIndex(self):
        if self.aktueller_knoten == self.anker:
            return -1
        index = 1
        knoten = self.anker.next
        while knoten != self.aktueller_knoten:
            knoten = knoten.next
            index += 1
        return index

    def AktuellesElement(self):
        return self.aktueller_knoten.inhalt if self.aktueller_knoten != self.anker else "Kein aktuelles Element"

    def Vor(self):
        if self.aktueller_knoten != self.anker:
            self.aktueller_knoten = self.aktueller_knoten.next

    def Zurück(self):
        if self.aktueller_knoten != self.anker:
            self.aktueller_knoten = self.aktueller_knoten.prev

    def Löschen(self):
        if self.aktueller_knoten != self.anker:
            self.aktueller_knoten.prev.next = self.aktueller_knoten.next
            self.aktueller_knoten.next.prev = self.aktueller_knoten.prev
            self.aktueller_knoten = self.aktueller_knoten.next if self.aktueller_knoten.next != self.anker else self.anker
            self.laenge -= 1

    def Länge(self):
        return self.laenge

    def __str__(self):
        ergebnis = []
        knoten = self.anker.next
        while knoten != self.anker:
            ergebnis.append(str(knoten.inhalt))
            knoten = knoten.next
        return " <-> ".join(ergebnis)


# Testprogramm
if __name__ == '__main__':
    liste = Schlange()
    liste.Einfügen('a')
    liste.Einfügen('b')
    liste.Einfügen('c')
    print("Liste nach Einfügen:", liste)
    
    liste.Vor()
    print("Aktuelles Element nach Vor():", liste.AktuellesElement())
    
    liste.Zurück()
    print("Aktuelles Element nach Zurück():", liste.AktuellesElement())
    
    liste.Löschen()
    print("Liste nach Löschen:", liste)
    
    liste.Positionieren(1)
    print("Element an Position 1:", liste.AktuellesElement())
