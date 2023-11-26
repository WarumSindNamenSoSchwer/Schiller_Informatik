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

clear() Entfernt alle Elemente
copy() Gibt Kopie zurück
fromkeys() Gibt Dictionary mit angegebenen Schlüsseln und Werten zurück
get() Gibt den Wert eines Schlüssels zurück
items() Gibt Liste mit Tuple (Schlüssel-Wert) zurück
keys() Gibt Liste mit Schlüsseln zurück
pop() Entfernt Element mit angegebenem Schlüssel
popitem() Entfernt letztes Schlüssel-Wert Paar
setdefault() Gibt Wert eines Schlüssels zurück oder fügt ihn ein
update() Aktualisiert das Dictionary mit Schlüssel-Wert Paar
values() Gibt Liste mit allen Werten zurück
'''