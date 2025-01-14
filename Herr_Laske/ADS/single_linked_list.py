
class Knoten:
    def __init__(self, daten):
        self.daten = daten
        self.nächster = None


class VerketteteListe:
    def __init__(self):
        self.front = None
        self.rear = None
        self.größe = 0

    def __str__(self) -> str:
        result = "front -> "
        aktueller_knoten = self.front
        while aktueller_knoten is not None:
            result += f"'{aktueller_knoten.daten}' -> "
            aktueller_knoten = aktueller_knoten.nächster
        result += "None"
        return result

    def size(self) -> int:
        return self.größe

    def is_empty(self) -> bool:
        return self.größe == 0

    def enqueue(self, item):
        neuer_knoten = Knoten(item)
        neuer_knoten.nächster = None
        
        if self.is_empty():
            self.front = neuer_knoten
            self.rear = neuer_knoten
        else:
            self.rear.nächster = neuer_knoten
            self.rear = neuer_knoten
        self.größe += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Die verkettete Liste ist leer, kann nichts entfernen.")
        item = self.front.daten
        self.front = self.front.nächster
        if self.front is None:
            self.rear = None
        self.größe -= 1
        return item

    def head(self):
        if self.is_empty():
            raise IndexError("Die verkettete Liste ist leer, kein Kopf vorhanden.")
        return self.front.daten
vl = VerketteteListe()

print("\n-------------Leer?-------------")
print("Empty: {}".format(vl.is_empty()))

print("\n-------------Liste:-------------")
print(str(vl))

print("\n-------------'one', 'two' und 'three' hinzufügen-------------")
vl.enqueue("one")
vl.enqueue("two")
vl.enqueue("three")

print("\n-------------Liste:-------------")
print(str(vl))

print("\n-------------Kopf?-------------")
print("Kopf: {}".format(vl.head()))

print("\n-------------Entfernen-------------")
print("Entfernt: {}".format(vl.dequeue()))
print("Entfernt: {}".format(vl.dequeue()))

print("\n-------------Liste:-------------")
print(str(vl))

print("\n-------------'four' & 'five' hinzufügen-------------")
vl.enqueue("four")
vl.enqueue("five")

print("\n-------------Liste:-------------")
print(str(vl))
