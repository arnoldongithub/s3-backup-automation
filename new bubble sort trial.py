def bubbleSort(arr):
    n=len(arr)

    #for loop to traverse through all elements in an array
    for i in range(n):
        for j in range(0,n-i-1):

            #Range of the array is from 0 to n-i-1
            #swap the elements if the element found is greater than the adjacent element
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

#driver code
#example tp test the above code
arr=[2,1,10,23]

bubbleSort(arr)

print("Sorted array is:")
for i in range(len(arr)):
    print(f"{arr[i]}")