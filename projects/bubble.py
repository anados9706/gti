
def sort(list):
    sorted = False

    while not sorted:
        sorted = True
        firstIdx = 0
        secondIdx = 1
        while secondIdx < len(list):
            first = list[firstIdx]
            second = list[secondIdx]
            if second < first:
                list[secondIdx] = first
                list[firstIdx] = second
                sorted = False
            secondIdx += 1
            firstIdx += 1     
    return list

if __name__ == "__main__":
    sorted = sort([7, 13, 22, 54, 23, 6, 100, 50, 2, 46])    
    print(sorted)