#Aufgabe 1
def addiere_zahlen(zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe

ergebnis = addiere_zahlen(5, 7)  # Das Ergebnis wird 12 sein


#Aufgabe 2
def begruesse_nutzer(name):
    begruessung = f"Hallo, {name}!"
    return begruessung

begruessungstext = begruesse_nutzer("Max")  # Das Ergebnis wird "Hallo, Max!" sein


#Aufgabe 3
def summe_zahlenreihe(bis_zahl):
    summe = 0
    zahl = 1

    while zahl <= bis_zahl:
        summe += zahl
        zahl += 1

    return summe

summe = summe_zahlenreihe(4)  # Das Ergebnis wird 10 sein (1 + 2 + 3 + 4)


#Aufgabe 4
def zaehle_zeichen(text):
    anzahl_zeichen = len(text)
    return anzahl_zeichen

laenge = zaehle_zeichen("Hallo")  # Das Ergebnis wird 5 sein
