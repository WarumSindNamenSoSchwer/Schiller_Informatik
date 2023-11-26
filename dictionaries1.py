'''
Thema: Dictionaries/Wörterbücher
Author: Muri
Date: 03.11.23
'''

'''
Dictionaries/Wörterbücher werden benutzt, um Datenwerte in Schlüssel:Wert Paaren zu speichern.

Dicts sind geordnete Sammlungen, die änderbar sind und keine Duplikate erlauben.

Erstellen:
'''

myDict = {
    "key" : "value", 
    "Marke" : "Apple",
    "GründungsDatum" : 1976,
    "Farben" : ["Rot", "Blau", "Grün"]
}

print(myDict)

'''
Um die Werte (values) der Schlüssel (keys) aufzurufen:

dict_name["key"]

Beispiel:
'''

print(myDict["Marke"])

'''
Wichtige Methoden von Dictonaries:

Methode         Beschreibung
clear()	        Entfernt alle Elemente des Wörterbuchs
copy()	        Gibt eine Kopie des Wörterbuchs wieder
fromkeys()	    Gibt ein Wörterbuch mit den angegeben Schlüsseln und Werten wieder
get()	        Gibt den Wert eines spezifischen Schlüssels wieder
items()	        Gibt eine Liste die ein Tuple beinhaltet mit den Schlüssel-Wert paaren 
keys()	        Gibt eine Liste die, die Schlüssel beinhaltet
pop()	        Entfernt das Element mit dem angegebenen Schlüssel
popitem()	    Entfernt das zu letzt hinzugefügt Schlüssel-Wert paar
setdefault()	Gibt den Wert eines spezifischen Schlüssels wieder. Wenn der Schlüssel nicht existiert: Füg den Schlüssel
                mit zugehörigen Wert ein
update()	    Aktualisiert das Wörterbuch mit dem angegebenen Schlüssel-Wert paar
values()	    Gibt eine Liste mit allen Werten des Wörterbuchs wieder
'''