# Bubble sort implementation
def bubbleSort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        # Traverse the array from 0 to n-i-1
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the adjacent element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test the above function
arr = [2, 1, 10, 23]
bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print("%d" % arr[i])
