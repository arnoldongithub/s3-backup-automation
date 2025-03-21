#selection sort algorithm in python
def selectionSort(array, size):
    for s in range(size):
        min_idx = s  # Setze das aktuelle Element als das kleinste

        for i in range(s + 1, size):
            # Suchen des kleinsten Elements im restlichen Array
            if array[i] < array[min_idx]:
                min_idx = i

        # Tausche das kleinste gefundene Element mit dem ersten Element der unsortierten Liste
        array[s], array[min_idx] = array[min_idx], array[s]

# Driver Code
data = [7, 2, 1, 6]
size = len(data)
selectionSort(data, size)

print("Sorted Array in Ascending Order is:")
print(data)
