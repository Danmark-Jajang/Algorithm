def InsertionSort(arr, n):  # arr: 무작위 배열, n: 배열의 길이
    for i in range(1, n): # 1부터 시작하는 이유는 시작하자마자 가장 왼쪽 인덱스는 정렬되었다고 가정 / 2번째 부터 n번째 까지(index상으로 1부터 n-1까지)
        loc = i-1 # 가장 최근 정렬된 위치, 처음에는 맨 앞 원소를 지정
        newItem = arr[i]
        while(loc>=0 and newItem<arr[loc]): # loc가 가장 앞으로 오거나 새로 삽입할 원소의 적합한 위치를 찾으면 while종료
            arr[loc+1] = arr[loc]  # 기존 정렬된 원소들을 한칸씩 뒤로 당김
            loc=loc-1
        arr[loc+1] = newItem
    return arr

arr1 = [0, 3, 5, 7, 2, 6, 8, 9, 1, 4]
arrS1 = InsertionSort(arr1, len(arr1))
print(arrS1)

arr2 = [12, 56, 93, 24, 5, 77, 92, 46, 13 ,35, 66]
arrS2 = InsertionSort(arr2, len(arr2))
print(arrS2)