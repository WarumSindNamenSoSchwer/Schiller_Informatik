#Aufgabe 1:
class Hund:
    def __init__(self, Name: str, Alter: int, Farbe: str) -> None:
        self.Name = Name
        self.Alter = Alter
        self.Farbe = Farbe

a = Hund('Bello', 3, 'Blau')

print(a.__dict__.values())

'''
Schritte:
1. Definieren Sie eine Klasse namens "Schülerin".
2. Legen Sie mindestens drei Attribute fest, um eine Schülerin zu beschreiben. Dazu gehören
beispielsweise Name, Alter und eine Liste von Fächern. Diese Liste soll zu Beginn leer sein.
3. Implementieren Sie eine Methode namens "anzeigen", die die Attribute der Schülerin aus-
gibt.
4. Implementieren Sie eine weitere Methode namens "fach_hinzufügen", die ein neues Fach
zur Liste der Fächer der Schülerin hinzufügt.
5. Erstellen Sie eine Instanz der Klasse "Schülerin" mit beliebigen Attributen und rufen Sie die
Methoden "anzeigen" und "fach_hinzufügen" auf, um Informationen über die Schülerin an- zuzeigen und ein neues Fach hinzuzufügen.
'''

#Aufgabe 2:
class Schülerin_list:
    def __init__(self, name: str, vorname: str, alter: int, fächer: list[str]) -> None:
        self.name: str = name
        self.vorname: str = vorname
        self.alter: int = alter
        self.fächer: list[str] = fächer

    def fach_hinzufügen(self, *neues_fach: str) -> str:
        for fach in neues_fach:
            self.fächer.append(fach)
        return 'Neue Liste: ', self.fächer

    def anzeigen(self) -> None:
        print(self.name, 
            self.vorname, 
            self.alter, 
            self.fächer
        )

s1 = Schülerin_list('Meric', 'Murat', 17, ['Deutsch', 'Englisch', 'Mathe'])
s1.fach_hinzufügen('Physik', 'Geschichte')
s1.anzeigen()

#Aufgabe 3:

class Schülerin_dict:
    def __init__( self, name: str, vorname: str, alter: int, fächer: dict[str, int] = None ) -> None:
        self.name: str = name
        self.vorname: str = vorname
        self.alter: int = alter
        self.fächer: dict[str, int] = fächer if fächer is not None else {}

    def fach_hinzufügen(self, neues_fach: dict[str, int]) -> str:
        for fach, note in neues_fach.items():
            self.fächer.update({fach: note if note is not None else 0})
            
    def anzeigen(self) -> None:
        print('+'+'-'*43+'+')

        print(f'|  Schüler/in:\t{self.vorname} {self.name}, Alter:\t{self.alter}  |')

        print('|'+'-'*43+'|')

        print(f'|\t{"Fach":<15}||\t{"Note":>10}  |')

        print('|'+'-'*22 + '||'+ '-'*19+'|')

        for fach, note in self.fächer.items():
            print(f'|\t{fach:<15}||\t{note:>10}  |')
        print('+'+'-'*43+'+')

s2 = Schülerin_dict('Meric', 'Murat', 17, {'Deutsch': 12, 'Englisch': 11, 'Mathe': 10})
s2.fach_hinzufügen({'Physik': 10, 'Geschichte': 12, 'Chemie': 11, 'Biologie': None})
s2.anzeigen()