
#def insertionSort(arr):
    #for i in range(1, len(arr)):
         #key = arr[i]
         #j = i-1
         #while j >=0 and key < arr[j] :
                 #arr[j+1] = arr[j]
                 #j -= 1
         #arr[j+1] = key     
#arr = [5, 23, 56, 8, 11, 2, 18, 99, 103]
#insertionSort(arr)
#print ("Sorted array is:")
#for i in range(len(arr)):
    #print ("%d" %arr[i])

def insertionSort(isort):
    for i in range(1, len(isort)):
        key = isort[i]
        j = i - 1
        while j >=0 and key < isort[j]:
            isort[j + 1] = isort[j]
            j -= 1
        isort[j + 1] = key
isort = [11, 72, 53, 47, 4, 18, 10, 90]  
insertionSort(isort)
print ("Sorted list is:", isort)
#for i in range (len(isort)):
    #print("%d" %isort[i])          
