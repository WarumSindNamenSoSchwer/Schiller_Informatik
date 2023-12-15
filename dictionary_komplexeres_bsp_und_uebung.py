# Autor: Philipp Schendel
# Datum: 11.12.2023
# Thema: Eingebettete Dictionaries

"""
Hier ein Beispiel für ein eingebettetes Dictionary:
"""

lehrkräfte = {"sdl":
                {"name": "Schendel",
                 "vorname": "Philipp",
                 "alter": 34,
                 "fächer":
                     {"Mathematik":["7E2", "8EU1", "MA_G4"],
                      "Informatik":["IN_G1","IN_G2",],
                      "ITG":["7E2", "7EU2"]
                     }
                 }
             }

# Es soll kontrolliert werden, ob zu den folgenden Kategorien Einträge
# vorhanden sind. Sind Werte vorhanden, sollen sie ausgegeben werden,
# andernfalls soll ein neuer Eintrag erstellt werden. (Kriegen Sie Teile
# davon sogar in einer Schleife und mit einer hübschen Ausgabe hin?)
kategorien = ["name", "vorname", "geburtsdatum"]

print('Kategorien:')
print(kategorien)

print(f'Lehrkräfte {list(lehrkräfte.keys())}')

for kat in kategorien:
        if kat not in lehrkräfte['sdl'].keys():
            neu = input('=> : ')
            lehrkräfte['sdl'][kat] = neu
            print(lehrkräfte)
            

# Fügen Sie das Fach Englisch hinzu, dass in der Klasse 8EU2 unterrichtet wird.

lehrkräfte['sdl']['fächer']['Englisch'] = ['8EU2']

# Fügen Sie zum Dictionary lehrkräfte eine neue Lehrkraft hinzu.

# Erstellen Sie ein ähnliches -- gern auch etwas abgespecktes -- Dictionary
# mit Schüler:innen, das ein weiteres Dictionary einbettet. Für jede Person
# sollen einige Noten für verschiedene Kurse erfasst sein. Berechnen Sie für
# jede Person eine Durchschnittsnote.

'''
frageliste = {"Frage 1": "Antwort 1",
              "Frage 2": "Antwort 2"}

punkte = 0

for frage in frageliste:
    i=3
    while i>0:
        guess = str(input(frage+" "))
        if guess == frageliste[frage]:
            print("Richtig! Du erhältst {i} Punkte.\n")
            punkte += i
            break
        elif guess != frageliste[frage] and i>1:
            print("Leider falsch! Versuchs noch einmal.\n")
            i-=1
        else:
            print(f"Leider falsch! Die Antwort war: {frageliste[frage]}.\n")
            break
            

'''
