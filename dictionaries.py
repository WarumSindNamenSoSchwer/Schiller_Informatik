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
Returns a dictionary with the specified keys and value
get()	        Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	    Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	    Updates the dictionary with the specified key-value pairs
values()	    Returns a list of all the values in the dictionary