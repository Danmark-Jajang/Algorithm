def HeapSort(arr, n):
    arr = buildHeap(arr, n)
    for i in range(n-1, 0, -1): # 맨 앞에 있는 가장 작은 값을 맨 뒤에 있는 값과 바꿈
        arr[0], arr[i] = arr[i], arr[0]
        heapfy(arr, 0, i) # 뒤에 들어간 작은 값을 제외한 배열을 수선하면 맨 앞에 그 다음으로 작은 값이 들어옴
    return arr

def buildHeap(arr, n):
    for i in range(n, -1, -1):
        heapfy(arr, i, n)
    return arr

def heapfy(arr, k, n): # k: 수선을 시작할 노드, n: 힙의 전체 크기
    left = (k+1)*2-1
    right = (k+1)*2
    if right < n:
        if arr[left] > arr[right]:
            smaller = right
        else:
            smaller = left
    elif left < n:
        smaller = left
    else:
        return
    
    if arr[k] > arr[smaller]:
        arr[smaller], arr[k] = arr[k], arr[smaller]
        heapfy(arr, smaller, n)
    return arr

arr1 = [4, 3, 5, 7, 2, 6, 8, 9, 1, 0]
arrS1 = HeapSort(arr1, len(arr1))
print(arrS1)

arr2 = [12, 56, 93, 24, 5, 77, 92, 46, 13 ,35, 66]
arrS2 = HeapSort(arr2, len(arr2))
print(arrS2)