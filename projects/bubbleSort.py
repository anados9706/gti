
#def bubbleSort(arr):
	#n = len(arr)

	#for i in range(n-1):
		#for j in range(0, n-i-1):
			#if arr[j] > arr[j + 1] :
				#arr[j], arr[j + 1] = arr[j + 1], arr[j]

#arr = [22, 7, 3, 12, 81, 9, 100, 46]

#bubbleSort(arr)

#print ("Sorted array is:")
#for i in range(len(arr)):
	#print ("% d" % arr[i],end=" ")

def bubbleSort(ulist):
	sorted = False

	while not sorted:
		sorted = True 
		firstIdx = 0
		secondIdx = 1
		while secondIdx < len(ulist):
			first = ulist[firstIdx]
			second = ulist[secondIdx]
			if second < first:
				ulist[firstIdx] = second
				ulist[secondIdx] = first
				sorted = False
			secondIdx += 1
			firstIdx += 1
	return ulist		

if __name__ == "__main__": 
	sorted = bubbleSort([2,100,35,64,8,19,6,40])
	print (sorted)