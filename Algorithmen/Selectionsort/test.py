def selecionsort(array, size):
    for ind in range(size):
        min_index = ind

        for j in range(ind + 1, size):
            if array[j] < array[min_index]:
                min_index = j

        (array[ind], array[min_index]) = (array[min_index], array[ind])

arr = [98, 22, 34, 48, 23, 37]
size = len(arr)
print(arr)
selecionsort(arr, size)
print(arr)


