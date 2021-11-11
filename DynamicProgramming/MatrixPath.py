def max(x, y):
    if x > y:
        return x
    else:
        return y

def MatrixPath(m, n): #m: 2차원 배열, n: n*n크기의 배열 지정
    c = [[ 0 for i in range(n)] for j in range(n)]
    c[0][0] = m[0][0]

    for i in range(1, n):
        c[i][0] = m[i][0] + c[i-1][0]
    for k in range(1, n):
        c[0][k] = m[0][k] + c[0][k-1]
    
    for i in range(1, n):
        for k in range(1, n):
            c[i][k] = m[i][k] + max(c[i-1][k], c[i][k-1])
    return c[n-1][n-1]

m1 = [[6, 7, 12, 5],
    [5, 3, 11, 18],
    [7, 17, 3, 3],
    [8, 10, 14, 9]]

m2 = [[2, 5, 8, 1],
    [2, 3, 7, 9],
    [4, 6, 10, 1],
    [2, 3, 5, 2]]
res1 = MatrixPath(m1, 4)
res2 = MatrixPath(m2, 4)
print(res1)
print(res2)
