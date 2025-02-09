### Ringbuffer
class RingBuffer:
    def __init__(self, maxsize):
        self.maxsize = maxsize #(maximale Anzahl der Plätze im Ring)
        self.ring = [] #Der Ring selbst
        self.anzahl = 0 #Anzahl der Elemente im Ring
        self.erster = 0 #Indexposition des ersten Elements
        for i in range (self.maxsize): #Erstellung eines leeren Rings mit der gegebenen maximalen Länge und Befüllung dieser Plätze mit None
            self.ring.append(None)


    def voll(self):
        if self.anzahl == 0:
            return False
        else:
            return self.erster == (self.erster+self.anzahl) % self.maxsize

    def leer(self):
        return self.anzahl == 0
            
    def add(self,wert):
        if self.voll():
            print ("Der Ringpuffer ist voll, es muss zunächst ein Element gelöscht werden!")
        else:
            i = (self.erster + self.anzahl)%self.maxsize
            self.ring[i] = wert
            print()
            print ("neuer eingefügter Wert: ", wert)
            self.anzahl = self.anzahl + 1
            print ("aktuell Anzahl der Elemente im Ringpuffer: ", self.anzahl)
        print ("Ringposition des Kopfes der Schlange (Indexpos):", self.erster)
        print ("Ringposition des Schwanzes der Schlange (Indexpos): ", (self.erster+self.anzahl)%self.maxsize-1)
        print()
        
        
    def get(self):
        if len (self.ring) == 0:
            print ("Der Ringpuffer ist leer!")
        else:
            print ("aktuelle Indexpos des Kopfes der Schlange: ", self.erster)
            #print ("aktueller Kopf der Schlange (Wert): ", self.get_Kopf())
            self.ring[self.erster] = None
            #x = self.ring.pop((self.erster+self.anzahl)%self.maxsize)
            self.erster = (self.erster+1)%self.maxsize
            self.anzahl = self.anzahl - 1
            print ("neuer aktuelle Indexpos des Kopfes der Schlange: ", self.erster)
            print ("neuer Wert des aktuellen Kopfes der Schlange: ", self.get_Kopf())
            return 

    def get_buffer(self):
        return self.ring

    def get_Kopf(self):
        return self.ring[self.erster]

    def freiePlaetze(self):
        return self.maxsize-self.anzahl


###Testprogramm###
r = RingBuffer(5)
print()
print ("aktueller Ringpuffer: ", r.get_buffer())
print ("Maximale Größe des Ringpuffers: ", r.freiePlaetze())
print()
print ("Ist der Ringpuffer voll: ", r.voll())
print ("Ist der Ringpuffer leer: ", r.leer())
print ()

print ("Hinzufügen von Zahlen!")
print ("----------------------")
r.add(43)
print ("aktueller Ring:", r.get_buffer())
print ("freie Plätze: ", r.freiePlaetze())
r.add(12)
print ("aktueller Ring:", r.get_buffer())
print ("freie Plätze: ", r.freiePlaetze())
r.add(35)
print ("aktueller Ring:", r.get_buffer())
print ("freie Plätze: ", r.freiePlaetze())
r.add(99)
print ("aktueller Ring:", r.get_buffer())
print ("freie Plätze: ", r.freiePlaetze())
r.add(22)
print ("aktueller Ring:", r.get_buffer())
print ("freie Plätze: ", r.freiePlaetze())
#r.add(68)
#print ("aktueller Ring:", r.get_buffer())
#print ("freie Plätze: ", r.freiePlaetze())
#r.add(54)
#print ("aktueller Ring:", r.get_buffer())
#print ("freie Plätze: ", r.freiePlaetze())
#r.add(77)
#print ("aktueller Ring:", r.get_buffer())
#print ("freie Plätze: ", r.freiePlaetze())
#print ()
#r.add(12)
#print ("aktueller Ring:", r.get_buffer())
#print ("freie Plätze: ", r.freiePlaetze())
print ()

print ("------------------------")
print ("Ist der Ringpuffer voll: ",r.voll())
print ("Entfernen des aktuellen Kopfes: ", r.get_Kopf())
r.get()
print ("aktueller Ring:", r.get_buffer())
print ("freie Plätze: ", r.freiePlaetze())
print ("Entfernen des aktuellen Kopfes: ", r.get_Kopf())
r.get()
print ("aktueller Ring:", r.get_buffer())
print ("freie Plätze: ", r.freiePlaetze())
print ()

print ("Hinzufügen einer neuen Zahl: ")
r.add(81)
print ("aktueller Ring:", r.get_buffer())
print ("freie Plätze: ", r.freiePlaetze())
r.add(33)
print ("aktueller Ring:", r.get_buffer())
print ("freie Plätze: ", r.freiePlaetze())


    
    


