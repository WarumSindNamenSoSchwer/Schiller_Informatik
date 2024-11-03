def InsertionSort(liste):

    for index in range(1, len(liste)):
        wert = liste[index]
        i = index - 1
        while i >= 0 and liste[i] > wert:
            liste[i + 1] = liste[i]
            i -= 1
        liste[i + 1] = wert
    return liste


Liste = [25, 17, 32, 56, 25, 19, 8, 66, 29, 6, 20, 29]
sorted_list = InsertionSort(Liste)
print(sorted_list)