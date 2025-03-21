#bubble sort algorithm
def bubbleSort(arr):
    n=len (arr)

    #transverse through all elements
    for i in range(n):
        swapped=False

        #Last i elements are already in place
        for j in range (0,n-i-1):

            #Transverse the array from 0 to n-i-1
            #swap if the element found is greater than the next element
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                swapped=True
            if(swapped==False):
                break

#Driver code to test the above
if __name__=="__main__":
    arr=[64,34,25,12,22,11,91,51]

    bubbleSort(arr)
    
    print("Sorted array")
    for i in range(len(arr)):
        print("%d"%arr[i],end="")