def QuickSort(arr, p, r): # arr: 무작위 배열, q: 시작 인덱스, r: 마지막 인덱스
    if p<r:
        q = partition(arr, p, r)
        QuickSort(arr, p, q-1)
        QuickSort(arr, q+1, r)
    return arr

def partition(arr, p, r): # 기준원소를 기준으로 좌우 분할 후 기준원소의 인덱스 반환
    center = arr[r]
    i = p-1
    for k in range(p, r):
        if center >= arr[k]: # 기준원소보다 작은 원소가 발견되면 왼쪽 그룹에 이동. 왼쪽 배열들의 가장 큰 인덱스 i를 사용하여 오른쪽 배열들의 가장 작은 인덱스와 교환
            i+=1
            arr[i], arr[k] = arr[k], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1


arr1 = [0, 3, 5, 7, 2, 6, 8, 9, 1, 4]
arrS1 = QuickSort(arr1, 0, len(arr1)-1)
print(arrS1)

arr2 = [12, 56, 93, 24, 5, 77, 92, 46, 13 ,35, 66]
arrS2 = QuickSort(arr2, 0, len(arr2)-1)
print(arrS2)