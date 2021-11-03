# 기본적으로 QuickSort알고리즘을 사용하고 이를 변형하여 구현
def Select(arr, p, r, i): # arr: 무작위 배열, p: 시작인덱스, r: 마지막 인덱스, i: i번째 작은 원소(index상으로 i-1의 원소)
    if p==r:
        return arr[p]

    q = partition(arr, p, r) # q: 기준원소의 절대적인 인덱스
    k=q-p+1
    if i==k:
        return arr[q]
    elif k<i:
        return Select(arr, q+1, r, i-k)
    else:
        return Select(arr, p, q-1, i)
    
def partition(arr, p, r):
    center = arr[r]
    i = p-1
    for k in range(p, r):
        if arr[k]<center:
            i+=1
            arr[i], arr[k] = arr[k], arr[i]
    arr[i+1], arr[r] = arr[r], arr[i+1]
    return i+1

arr1 = [0, 3, 5, 7, 2, 6, 8, 9, 1, 4]
arrS1 = Select(arr1, 0, len(arr1)-1, 4)
print(arrS1)

arr2 = [12, 56, 93, 24, 5, 77, 92, 46, 13 ,35, 66]
arrS2 = Select(arr2, 0, len(arr2)-1, 5)
print(arrS2)