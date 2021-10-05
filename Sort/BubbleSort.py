def BubbleSort(arr, n): #arr: array, n: size of array
    for i in range(n-1, 0, -1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

arr1 = [0, 3, 5, 7, 2, 6, 8, 9, 1, 4]
arrS1 = BubbleSort(arr1, len(arr1))
print(arrS1)

arr2 = [12, 56, 93, 24, 5, 77, 92, 46, 13 ,35, 66]
arrS2 = BubbleSort(arr2, len(arr2))
print(arrS2)