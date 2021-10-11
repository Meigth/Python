def multiply_matrix(A1, B1):
    res = [[] for _ in range(len(A1))]

    for i in range(len(A1)):
        for j in range(len(B1[0])):
            sum = 0
            for k in range(len(A1[0])):
                sum += A1[i][k] * B1[k][j]
            res[i] += [sum]

    return res

def power_matrix(A1, l):
    if l == 2:
        return multiply_matrix(A1, A1)
    else:
        return multiply_matrix(A1, power_matrix(A1, l - 1))

n = int(input())
A = [[int(i) for i in input().split()] for _ in range(n)]
st = int(input())
C = power_matrix(A, st)
[print(*i) for i in C]