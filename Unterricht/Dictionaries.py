'''
Thema: Dictionaries/Wörterbücher
Author: Muri
Date: 03.11.23
'''

'''
Dictionaries/Wörterbücher speichern Daten in Schlüssel:Wert Paaren.

Dicts sind geordnet, änderbar und erlauben keine Duplikate.

Erstellen:
'''

myDict = {
"key": "value",
"Marke": "Apple",
"GründungsDatum": 1976,
"Farben": ["Rot", "Blau", "Grün"]
}

print(myDict)

'''
Zugriff auf Werte:
'''

print(myDict["Marke"])

'''
Wichtige Methoden:

Methoden:       Beschreibung:

clear()         Entfernt alle Elemente
copy()          Gibt Kopie zurück
fromkeys()      Gibt Dictionary mit angegebenen Schlüsseln und Werten zurück
get()           Gibt den Wert eines Schlüssels zurück
items()         Gibt Liste mit Tuple (Schlüssel-Wert) zurück
keys()          Gibt Liste mit Schlüsseln zurück
pop()           Entfernt Element mit angegebenem Schlüssel
popitem()       Entfernt letztes Schlüssel-Wert Paar
setdefault()    Gibt Wert eines Schlüssels zurück oder fügt ihn ein
update()        Aktualisiert das Dictionary mit Schlüssel-Wert Paar
values()        Gibt Liste mit allen Werten zurück
'''

# Beispiel-Dictionary
myDict2 = {
    "Name": "Muri",
    "Alter": 16,
    "Beruf": "Schüler"
}

myDict2.clear()
print(myDict2)  # Ausgabe: {}

original_dict = {"A": 1, "B": 2}
copy_dict = original_dict.copy()
print(copy_dict)  # Ausgabe: {"A": 1, "B": 2}

alter = myDict2.get("Alter")
print(alter)  # Ausgabe: "None", da "Alter" nicht im leeren Dictionary vorhanden ist

items_list = original_dict.items()
print(items_list)  # Ausgabe: dict_items([('A', 1), ('B', 2)])

keys_list = original_dict.keys()
print(keys_list)  # Ausgabe: dict_keys(['A', 'B'])

value_removed = original_dict.pop("A")
print(value_removed)  # Ausgabe: 1, und original_dict wird zu {'B': 2}

last_item = original_dict.popitem()
print(last_item)  # Ausgabe: ('B', 2), und original_dict wird zu {}

name = myDict2.setdefault("Name", "Default Name")
print(name)  # Ausgabe: Default Name, da "Name" bereits im leeren Dictionary existiert

original_dict.update({"C": 3})
print(original_dict)  # Ausgabe: {'B': 2, 'C': 3}

values_list = original_dict.values()
print(values_list)  # Ausgabe: dict_values([2, 3])

'''
Aufgabe 1:
Erstelle ein leeres Dictionary mit dem Namen person.

Aufgabe 2:
Füge dem Dictionary person folgende Schlüssel-Wert-Paare hinzu:

"Name" mit dem Wert "Alice"
"Alter" mit dem Wert 30
"Stadt" mit dem Wert "Berlin"

Aufgabe 3:
Drucke den Wert des Schlüssels "Alter" aus dem Dictionary person.

Aufgabe 4:
Überprüfe, ob der Schlüssel "Geschlecht" im Dictionary person vorhanden ist. Falls nicht, 
füge einen neuen Schlüssel "Geschlecht" mit dem Wert "weiblich" hinzu.

Aufgabe 5:
Erstelle ein neues Dictionary adresse mit den Schlüsseln und Werten:

"Straße": "Hauptstraße 123"
"PLZ": "12345"
"Land": "Deutschland"
Füge dann alle Schlüssel-Wert-Paare aus dem Dictionary adresse dem Dictionary person hinzu.

Aufgabe 6:
Drucke alle Schlüssel im Dictionary person.

Aufgabe 7:
Entferne den Schlüssel "Stadt" aus dem Dictionary person

Aufgabe 8: (for-Schleife)
Verwende eine for-Schleife, um alle Schlüssel und Werte im Dictionary person zu drucken.

Aufgabe 9: (while-Schleife)
Erstelle eine while-Schleife, die solange läuft, bis das Alter der Person größer als 35 ist. In jedem 
Schritt der Schleife erhöhe das Alter um 1.

Aufgabe 10: (Turtle und Dictionary)
Erstelle ein Dictionary namens "farben_dict" mit den Schlüsseln "rot", "blau" und "grün", wobei 
die Werte Tupel sind, die die RGB-Werte der entsprechenden Farben repräsentieren (zur erinnerung farbe(r,g,b) ,die 
Werte gehen von 0 bis 1, wobei 1 immer für die volle und 0 für die schwächste Intensität steht, die werte können 
auch als float -> 0.5 z.B. angegeben werden kann).
Verwende dann die Turtle-Grafikbibliothek, um drei Quadrate nebeneinander zu zeichnen, wobei 
jedes Quadrat eine der Farben aus dem Dictionary verwendet. Nutze eine Schleife, um dies effizient zu tun.

Aufgabe 11: (Turtle, Dictionary und while-Schleife)
Erstelle ein Dictionary "bewegungen" mit den Schlüsseln "vorwärts", "rückwärts", "links" und "rechts", 
wobei die Werte die entsprechenden Bewegungen in der Turtle-Grafik sind.
Lass die Turtle dann durch eine while-Schleife Benutzereingaben entgegennehmen. Bei jeder Eingabe soll 
die Turtle die entsprechende Bewegung gemäß dem Dictionary "bewegungen" ausführen. Die Schleife soll solange 
laufen, bis der Benutzer "exit" eingibt.
'''