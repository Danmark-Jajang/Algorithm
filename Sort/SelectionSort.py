def SelectionSort(arr, n): # arr: 무작위 배열, n: 배열의 길이
    for i in range(n-1, 0, -1): # n번째부터 2번째까지(index상으로 n-1부터 1까지)
        largest = theLargest(arr, i) # 가장 큰 값을 가지고 있는 배열의 index반환
        arr[i], arr[largest] = arr[largest], arr[i] #가장 큰 값을 맨 뒤로 보냄
    return arr

def theLargest(arr, last): # 가장 큰 값을 가지고 있는 배열의 index반환
    largest = 0 # 맨 앞의 인덱스
    for i in range(last+1): # 첫 번째부터 last까지(index상으로 0부터 last-1까지)
        if(arr[i]>arr[largest]):
            largest = i
    return largest

arr1 = [0, 3, 5, 7, 2, 6, 8, 9, 1, 4]
arrS1 = SelectionSort(arr1, len(arr1))
print(arrS1)

arr2 = [12, 56, 93, 24, 5, 77, 92, 46, 13 ,35, 66]
arrS2 = SelectionSort(arr2, len(arr2))
print(arrS2)