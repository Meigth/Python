def multiply_matrix(A1, B1):
    res = [[] for _ in range(len(A1))]

    for i in range(len(A1)):
        for j in range(len(B1[0])):
            sum = 0
            for k in range(len(A1[0])):
                sum += A1[i][k] * B1[k][j]
            res[i] += [sum]

    return res


n, m = [int(i) for i in input().split()]
A = [[int(i) for i in input().split()] for _ in range(n)]
input()
l, h = [int(i) for i in input().split()]
B = [[int(i) for i in input().split()] for _ in range(l)]
C = multiply_matrix(A, B)
[print(*i) for i in C]