def bubble_sort(array):
    #loop um durch liste zu iterrieren
    for n in range(len(array) - 1, 0, -1):
        #elemente vergleichen
        for i in range(n):
            if array[i] > array[i + 1]:
                #elemente vertauschen
                array[i], array[i + 1] = array[i + 1], array[i]
array = [57, 18, 45, 98, 120, 45, 1, 22]
print(f"Unsortiert: {array}")
bubble_sort(array)
print(f"Sortiert: {array}")

#laufzeit ist immer O(n^2) kleine elemente werden eher langsam nach vorne sortiert wenn man aufsteigend sortiert
