import time
import matplotlib.pyplot as plt

def bubble_sort(array):
    for n in range(len(array) - 1, 0, -1):
        for i in range(n):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]

def insertion_sort(array):
    for index in range(1, len(array)):
        value = array[index]
        i = index - 1
        while i >= 0 and array[i] > value:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = value
    return array

def quick_sort(arr):
    elements = len(arr)
    if elements < 2:
        return arr
    pivot_index = 0
    for i in range(1, elements):
        if arr[i] <= arr[0]:
            pivot_index += 1
            arr[i], arr[pivot_index] = arr[pivot_index], arr[i]
    arr[0], arr[pivot_index] = arr[pivot_index], arr[0]
    left = quick_sort(arr[:pivot_index])
    right = quick_sort(arr[pivot_index + 1:])
    return left + [arr[pivot_index]] + right

def selection_sort(array):
    size = len(array)
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]


def time_algorithm(algorithm, array):
    start_time = time.perf_counter()
    algorithm(array.copy()) 
    return time.perf_counter() - start_time

array = [35, 28, 41, 7, 14, 50, 33, 21, 21, 60, 18, 12] #* 100

algorithms = {
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort,
    "Selection Sort": selection_sort
}

times = {}
for name, algorithm in algorithms.items():
    times[name] = time_algorithm(algorithm, array)
    
plt.figure(figsize=(10, 6))
plt.bar(times.keys(), times.values(), color=['blue', 'green', 'red', 'orange'])
plt.xlabel('Sorting Algorithm')
plt.ylabel('Time (seconds)')
plt.title('Time Complexity Comparison of Sorting Algorithms')
plt.show()