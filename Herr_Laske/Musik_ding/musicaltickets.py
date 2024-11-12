#----------------------------------------------------
# Dateiname: musicaltickets.py
# Verwaltung eines Musicals - Kartenverkauf
# Objektorientierte Programmierung mit Python
#----------------------------------------------------

import pickle
from musical import *

class Kartenverkauf:
    __menuetext = '''
    Musical-Ticketservice
    ---------------------
    (B)uchung
    (U)eberblick Vorstellungen
    (E)nde
    '''

    def __init__(self, datei):
        self.__datei = datei
        self.__lade_musical()
        self.__run()

    def __lade_musical(self): 
        ''' versucht, aus Datei Musical zu laden'''
        try:
            f = open(self.__datei, 'rb')
            self.__musical = pickle.load(f)
            f.close()
            print('\n              W I L L K O M M E N')
            print('beim Buchungssystem für das Musical', 
                  self.__musical.titel)
        except:
            print('Kein Musical gespeichert. ')

    def __run(self):
        ''' Menü und Verarbeitung von Auswahlen'''
        print(self.__menuetext)
        wahl = '-'
        while wahl not in 'eE':
            wahl = input('Auswahl: ')
            if wahl in 'bB': self.__buchen()
            elif wahl in 'gG':
                v = self.__musical.getVorstellung('1. 10. 2010')
                v.get_zuschauer()
            elif wahl in 'uU': print(self.__musical)
            print(self.__menuetext)
        print('Danke für die Benutzung von Musical-Ticketservice')
        self.__speichern()

    def __buchen(self):                               #1
        '''Dialog zum Buchen mehrerer Plätze '''
        datum = input('Datum der Vorstellung: ')
        vorstellung = self.__musical.getVorstellung(datum)
        if not vorstellung:                           #2
            print('An diesem Tag gibt es keine Vorstellung')
        else:
          print(vorstellung.saalbelegung)
          name = input('Name: ')
          tel = input('Telefonnummer: ')
          zuschauer = Zuschauer(name, tel)
          reihe = 'x'                                 #3 
          while reihe != '':
            reihe = input('Reihe: ')
            if reihe != '':                           #4
                platz = input('Platz: ')
                print(vorstellung.saalbelegung.buche(
                  int(reihe)-1, int(platz) - 1, zuschauer))
            self.__eintrittskarte(name, reihe, platz, datum, vorstellung)

#Aufgabe 1 Eintrittskarte
    def __eintrittskarte(self, name, reihe, platz, datum, vorstellung):
        karte = f"""--------------------
Eintrittskarte
{self.__musical.titel}
Name      : {name}
Reihe     : {reihe}
Platz     : {platz}
Datum     : {datum}
Beginn    : {vorstellung.beginn}
Zuschauer : {vorstellung.get_zuschauer}
Preis     : {self.__musical.eintrittspreis}
--------------------
"""
        #-> wrm nt : self.vorstellung.beginn? analog zu self.__musical.titel
        print(karte)


    def __speichern(self):
        f = open(self.__datei, 'wb')
        pickle.dump(self.__musical, f)
        f.close()

kasse1 = Kartenverkauf('Herr_Laske\Musik_ding\daten\hairspray.txt')
