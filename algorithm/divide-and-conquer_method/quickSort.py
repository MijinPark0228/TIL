def partition(partitionList, n):
    left = 1
    right = n-1

    while left < right :
        while left < n and partitionList[left] < partitionList[0] :
            left += 1
        while right > 0 and partitionList[right] >= partitionList[0] :
            right -= 1

        if left < right :
            temp = partitionList[left]
            partitionList[left] = partitionList[right]
            partitionList[right] = temp
        else:
            temp = partitionList[0]
            partitionList[0] = partitionList[right]
            partitionList[right] = temp

    return right


def insertArray(returnArray, insertArray, startKey):
    for index, value in enumerate(insertArray):
        returnArray[startKey + index] = value

def quick_sort(sortList, n):
    if n > 1 :
        pivot = partition(sortList[0:n], n)
        leftTemp = sortList[0:pivot]
        quick_sort(leftTemp, pivot)
        insertArray(sortList, leftTemp, 0)

        rightTemp = sortList[pivot + 1:n]
        quick_sort(sortList[pivot + 1:n], n - pivot - 1)
        insertArray(sortList, rightTemp, pivot + 1)

testA = [0,30,20,10,5,4,3,1,80,90,75]
lengthByTestA = len(testA)
quick_sort(testA, lengthByTestA)
print(testA)