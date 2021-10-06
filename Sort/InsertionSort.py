def InsertionSort(arr, n): #arr: array, n: size of array, 시작하자마자 가장 왼쪽 인덱스는 정렬되었다고 가정
    for i in range(1, n):
        loc = i-1 #last sorted position
        newItem = arr[i]
        while(loc>=0 and newItem<arr[loc]):
            arr[loc+1] = arr[loc]
            loc=loc-1
        arr[loc+1] = newItem
    return arr

arr1 = [0, 3, 5, 7, 2, 6, 8, 9, 1, 4]
arrS1 = InsertionSort(arr1, len(arr1))
print(arrS1)

arr2 = [12, 56, 93, 24, 5, 77, 92, 46, 13 ,35, 66]
arrS2 = InsertionSort(arr2, len(arr2))
print(arrS2)