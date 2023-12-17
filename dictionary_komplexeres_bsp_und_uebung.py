# Autor: Philipp Schendel
# Datum: 11.12.2023
# Thema: Eingebettete Dictionaries

"""
Hier ein Beispiel für ein eingebettetes Dictionary:
"""
'''
lehrkräfte ={"sdl":
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
lehrer_namen = list(lehrkräfte.keys())

kategorien = ["name", "vorname", "geburtsdatum"]

for lehrer_name in lehrer_namen:
    print(f"\nLehrer: {lehrer_name}")

    for kat in kategorien:
        if kat in lehrkräfte[lehrer_name]:
            print(f'{kat.capitalize()}: {lehrkräfte[lehrer_name][kat]}')
        else:
            neu = input(f'Geben Sie einen Wert für {kat.capitalize()} ein: ')
            lehrkräfte[lehrer_name][kat] = neu

print("\nAktualisiertes Dictionary:")
print(lehrkräfte)
            

# Fügen Sie das Fach Englisch hinzu, dass in der Klasse 8EU2 unterrichtet wird.

lehrkräfte['sdl']['fächer']['Englisch'] = ['8EU2']

# Fügen Sie zum Dictionary lehrkräfte eine neue Lehrkraft hinzu.

neue_lehrkraft ={
'Ra':
    {
        'name' : 'Rausch',
        'vorname' : 'Jennefer',
        'alter' : None,
        'fächer' : 
            {
            'Mathematik' : ['7EU1', '9E2'],
            'Französisch' : ['8G', '10EU1']
        }
    }
}

lehrkräfte.update(neue_lehrkraft)
print(lehrkräfte)
'''

# Erstellen Sie ein ähnliches -- gern auch etwas abgespecktes -- Dictionary
# mit Schüler:innen, das ein weiteres Dictionary einbettet. Für jede Person
# sollen einige Noten für verschiedene Kurse erfasst sein.

# Schreiben Sie eine Funktion, die ein SuS-Dictionary bekommt und zu jeder Person
# die Durchschnittsnote berechnet.

schueler_dict = {
    1:{
        'vorname' : 'Murat',
        'nachname' : 'Meric',
        'fächer' :{
            'physik' : 12,
            'geschichte' : 11,
            'mathe' : 10
        }
    },
    2:{
        'vorname' : 'Amin',
        'nachname' : 'Gerhab',
        'fächer' :{
            'franz' : 15,
            'philo' : 6,
            'englisch' : 15
        }
    }
}   


def durchschnittsnote(SuS_dict):
    for schueler_id, daten in SuS_dict.items():
        noten = daten['fächer'].values()
        durchschnitt = sum(noten) / len(noten)
        print(f"{daten['vorname']} {daten['nachname']}: Durchschnittsnote {durchschnitt:.2f}")
    
        
durchschnittsnote(schueler_dict)

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

fhfhhfe
'''
