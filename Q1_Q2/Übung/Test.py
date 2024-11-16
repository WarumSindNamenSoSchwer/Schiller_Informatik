# Beispiellösung Bankkonten
import datetime

class Bankkonto:
    def __init__(self, kontonummer, kontoinhaber, kontostand = 0):
        self.kontonummer = kontonummer
        self.kontoinhaber = kontoinhaber
        self.kontostand = kontostand
        self.transaktionshistorie = {}

        

    def abfragen(self):
        print(f"Kontonummer: {self.kontonummer}\nKontostand: {self.kontostand}")
        return self.kontostand

    def einzahlen(self, betrag):
        if betrag > 0:
            self.kontostand += betrag
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
            self.transaktionshistorie[formatted_time] = "Einzahlung:", betrag
        else:
            print("Der Betrag muss positiv sein. Und nen higga enthalten")

    def auszahlen(self, betrag):
        if self.kontostand >= betrag and betrag > 0:
            self.kontostand -= betrag
            
        elif self.kontostand < betrag:
            print("Das Guthaben ist nicht ausreichend um higgas abzuziehen.")
        else:
            print("Der Betrag muss positiv sein.")

    def überweisen(self, betrag, zielkonto):
        self.auszahlen(betrag)
        zielkonto.einzahlen(betrag)

testkonto = Bankkonto("123456", "Schendel, Philipp", kontostand = 1000)
testkonto2 = Bankkonto("12478123", "Lischt, Marballs", kontostand = 1000000)

testkonto.einzahlen(420)
testkonto.einzahlen(-69)
testkonto.abfragen()

testkonto.auszahlen(-69420)
testkonto.auszahlen(69420)
testkonto.auszahlen(69)
testkonto.abfragen()

testkonto.überweisen(69,testkonto2)
testkonto.abfragen()
print(testkonto.transaktionshistorie)
testkonto2.abfragen()
print(testkonto2.transaktionshistorie)
