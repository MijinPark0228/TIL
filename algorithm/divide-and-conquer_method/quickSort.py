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
            temp = partitionList[left]
            partitionList[left] = partitionList[right]
            partitionList[right] = temp

    return right


def quick_sort(sortList, n):
    if n > 1 :
        pivot = partition(sortList[0:n-1], n)
        quick_sort(sortList[0:pivot, pivot])
        quick_sort(sortList[pivot + 1:n-1], n - pivot - 1)

testA = [0,30,20,10,5,4,3,1,80,90,75]
print (len(testA))
quick_sort(testA, len(testA))
print(vars(testA))