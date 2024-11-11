#----------------------------------------------------
# Dateiname: musicalmanager.py
# Verwaltung eines Musicals - Manager
# Objektorientierte Programmierung mit Python
#----------------------------------------------------

# musicalmanager.py  - Verwaltung eines Musicals 
import pickle
from musical import *

class Manager:   
    __menuetext = """
    Musical-Manager
    ------------------
    (n)eue Vorstellung
    (U)eberblick Vorstellungen
    (E)nde
     """

    def __init__(self, datei):                        #1
        self.__datei = datei  
        self.__lade_musical()
        self.__run()

    def __run(self):                                  #2
        """ Menü und Verarbeitung von Auswahlen"""
        print (self.__menuetext)
        wahl = '-'
        while wahl not in ['e', 'E']:
          wahl = input('Auswahl: ')
          if wahl in ['n', 'N']:
            self.__neueVorstellung()
          elif wahl in ['U', 'u']: 
            print (str(self.__musical))
            print (self.__menuetext)
            wahl = input('Auswahl: ')
        print ("Danke für die Benutzung von Musical-Manager")
        self.__speichern()

    def __neueVorstellung(self):
        """Dialog zum Einrichten einer neuen Vorstellung"""
        datum = input('Termin: ')
        beginn = input('Beginn der Vorstellung: ')
        vorstellung = Vorstellung(datum, beginn, self.__musical.saal)
        self.__musical.neueVorstellung(vorstellung)

    def __neuesMusical(self):                        #3
        '''Dialog zur Definition eines neuen Musicals'''
        titel = input('Titel: ')
        eintrittspreis = float(input('Eintrittspreis: '))
        anzahl_reihen = int(input("Anzahl Sitzreihen: "))
        liste = []
        for i in range(anzahl_reihen):
            sitze = int(input("Sitze in Reihe " + str(i) + ": "))
            liste.append(sitze)                 
        saal = Saal(liste)
        self.__musical = Musical(titel, eintrittspreis, saal)

    def __lade_musical(self): 
        """Musical-Objekt wird geladen, falls Datei vorhanden
        sonst muss neues Musical definiert werden"""
        try:
            f = open(self.__datei, 'rb')  # lesen im Binärmodus
            self.__musical = pickle.load(f)
            f.close()
            print ('\n               W I L L K O M M E N')
            print ('beim Management-System für das Musical',
                   self.__musical.titel)
        except:
            print('Kein Musical gespeichert.')
            print('Richten Sie neues Musical ein.')
            self.__neuesMusical()

    def __speichern(self):                           
        """Musical-Objekt speichern """
        f = open(self.__datei, 'wb') # schreiben im Binärmodus
        pickle.dump(self.__musical, f)
        f.close()

m = Manager('daten/hairspray.txt')   # relative Adresse der Daten-Datei
