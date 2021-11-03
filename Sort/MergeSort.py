import sys
sys.setrecursionlimit(10**6) # 재귀함수 깊이 제한 해제

def MergeSort(arr, p, r): # arr: 무작위 배열, p: 배열 시작 인덱스, r: 배열 마지막 인덱스
    if(p<r):
        q = (int)((p+r)/2)
        MergeSort(arr, p, q)
        MergeSort(arr, q+1, r)
        Merge(arr, p, q, r)
    return arr

def Merge(arr, p, q, r): # 병합
    tmp = [0 for i in range(r-p+1)]
    i = p
    k = q+1
    t = 0
    while(i<=q and k<=r): # merge된 두 배열을 돌면서 하나의 배열 내용을 먼저 다 꺼낼 때 까지 반복
        if arr[i] < arr[k]: # 작은 merge된 두 배열의 앞 부분 원소의 크기를 비교해 작은 원소부터 채워넣는다
            tmp[t] = arr[i]
            t+=1
            i+=1
        else:
            tmp[t] = arr[k]
            t+=1
            k+=1

    # 남은 배열을 tmp에 집어넣는다
    while(i<=q):
        tmp[t] = arr[i]
        t+=1
        i+=1
    while(k<=r):
        tmp[t] = arr[k]
        t+=1
        k+=1

    # merge된 배열을 arr로 옮긴다
    i = p
    t = 0
    while(i<=r):
        arr[i] = tmp[t]
        i+=1
        t+=1
    return arr

arr1 = [0, 3, 5, 7, 2, 6, 8, 9, 1, 4]
arrS1 = MergeSort(arr1, 0, len(arr1)-1)
print(arrS1)

arr2 = [12, 56, 93, 24, 5, 77, 92, 46, 13 ,35, 66]
arrS2 = MergeSort(arr2, 0, len(arr2)-1)
print(arrS2)
