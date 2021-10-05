def SelectionSort(arr, n): # arr: array, n: size of arr
    for i in range(n-1, 0, -1):
        largest = theLargest(arr, i) # largest number's index
        arr[i], arr[largest] = arr[largest], arr[i]
    return arr

def theLargest(arr, last): # return largest number's index
    largest = 0
    for i in range(last+1): # 0~(last-1)+1
        if(arr[i]>arr[largest]):
            largest = i
    return largest

arr1 = [0, 3, 5, 7, 2, 6, 8, 9, 1, 4]
arrS1 = SelectionSort(arr1, len(arr1))
print(arrS1)

arr2 = [12, 56, 93, 24, 5, 77, 92, 46, 13 ,35, 66]
arrS2 = SelectionSort(arr2, len(arr2))
print(arrS2)