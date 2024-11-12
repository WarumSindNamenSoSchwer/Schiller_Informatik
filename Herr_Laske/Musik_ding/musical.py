#----------------------------------------------------
# Dateiname: musical.py
# Modul mit Klassen zur Modellierung eines Musicals
# Objektorientierte Programmierung mit Python
#----------------------------------------------------²


# musical.py  - Modell eines Musicals

import pickle

class Musical: 
    def __init__(self, titel, eintrittspreis, saal):
       self.titel = titel
       self.eintrittspreis = eintrittspreis
       self.saal = saal
       self.vorstellungen = [] # Liste von Vorstellungen

    def getVorstellung(self, datum):
        """Rückgabe eines Vorstellungs-Objektes mit
        passendem Datum, falls vorhanden, sonst None"""        
        for vorstellung in self.vorstellungen:
          if vorstellung.datum == datum: return vorstellung
        # Nach dem return bricht die Ausführung der Funktion ab

    def neueVorstellung(self, vorstellung):
        """Objekt vorstellung wird in Liste eingefügt"""
        self.vorstellungen += [vorstellung]

    def storniere(self, datum):
        for vorstellung in self.vorstellungen:
            if vorstellung.datum == datum:
                self.vorstellungen.remove(vorstellung)
                zuschauer_info = "Stornierte Vorstellung: Zuschauer und Telefonnummern:\n"
                for reihe in vorstellung.saalbelegung.belegung:
                    for platz in reihe:
                        if platz.belegt():
                            zuschauer = platz.zuschauer
                            zuschauer_info += f"{zuschauer.name}, Tel: {zuschauer.tel}\n"
                return zuschauer_info
        return "Keine Vorstellung mit diesem Datum gefunden."
    
    def __str__(self):                               #1
        beschreibung = '\n' + self.titel + '\n' + \
                       len(self.titel)*'=' + '\n'
        for vorstellung in self.vorstellungen:
            beschreibung += str(vorstellung) + '\n'
        return beschreibung 


class Vorstellung:
    def __init__(self, datum, beginn, saal ):
        self.datum = datum
        self.beginn = beginn
        self.saalbelegung = Saalbelegung(saal)
        self.saal = saal

    def __str__(self):                               #1
        beschreibung = self.datum + '\n' + \
        str(self.saalbelegung.getFreiePlaetze()) + \
        ' freie Plätze\n' 
        return beschreibung

    def get_zuschauer(self) -> str:
        # gibt liste von Zuschauern aus und zeigt an welche plätze noch nicht belegt sind
        zuschauer: list[str] = []
        for reihe in self.saalbelegung.belegung:
            for platz in reihe:
                if platz.belegt():
                    zuschauer.append(platz.zuschauer.name)
        return ", ".join(zuschauer)
    
    # Gibt eine lesbarere Liste der Zuschauer mit Sitzplatzinformationen zurück
    '''def get_zuschauer(self) -> str: 
        zuschauer_liste = []
        reihen_nummer = 1
        for reihe in self.saalbelegung.belegung:
            platz_nummer = 1
            for platz in reihe:
                if platz.belegt():
                    zuschauer_liste.append(f"\tReihe {reihen_nummer}, Platz {platz_nummer}: {platz.zuschauer.name} (Tel: {platz.zuschauer.tel})")
                platz_nummer += 1
            reihen_nummer += 1
        if zuschauer_liste:
            return "\nListe der Zuschauer:\n" + "\n".join(zuschauer_liste)
        else:
            return "Keine Zuschauer belegt."'''
        
    
class Saalbelegung:
    """pflegt Liste von Listen mit Platz-Objekten"""
    def __init__(self, saal):
        self.belegung = []
        self.saal = saal
        for i in range(len(saal.plaetzeProReihe)):   #2
            reihe = []
            for j in range(saal.plaetzeProReihe[i]):
                platz = Platz()
                reihe += [platz]
            self.belegung += [reihe]

    def buche(self, reihe, platz, zuschauer):        #3
        '''weist dem Platz platz in Reihe reihe einen
        Zuschauer zu'''
        if not self.belegung[reihe][platz].belegt():
           self.belegung[reihe][platz].belege(zuschauer)
           return 'Platz gebucht'
        else: return 'Platz schon belegt'

    def getFreiePlaetze(self):
        """liefert Anzahl der freien Plaetze"""
        frei=0
        for reihe in self.belegung:
            for platz in reihe:
                if not platz.belegt(): frei += 1
        return frei

    def __str__(self):                               #1
        beschreibung = 'Saalbelegung\n'
        beschreibung += '   Platz: 1  2  3  4  5  6  7  8  9  10 '
        beschreibung += '11 12 13 14\n'
        nr = 1                           # Reihennummer
        for reihe in self.belegung:
            beschreibung += 'Reihe ' + format(nr, '2d') + ': '
            for platz in reihe:
                beschreibung += str(platz)
            nr += 1
            beschreibung += '\n'         # neue Zeile
        return beschreibung

class Zuschauer:
    def __init__(self, name, tel):
        self.name, self.tel = name, tel

class Platz:
    def __init__(self):
        self.zuschauer = None

    def belegt(self):
        if self.zuschauer: return True
        else: return False

    def belege(self, zuschauer):
        self.zuschauer = zuschauer

    def __str__(self):                              #1
        if self.belegt():
            return self.zuschauer.name[:2] + ' '   
            # vom Zuschauername nur die ersten beiden Zeichen   
        else:
            return '-- '       # freier Platz

class Saal:
    def __init__(self, liste):
        self.plaetzeProReihe = liste


    
