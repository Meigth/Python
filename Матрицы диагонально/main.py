n, m = [int(i) for i in input().split()]
res = [[0] * m for i in range(n)]
res[0][0] = 1
cn = 1

for i in range(1, m):
    res[0][i] = res[0][i - 1] + cn
    if cn < n:
        cn += 1

for i in range(1, n):
    res[i][-1] = res[i - 1][-1] + cn
    if cn > 2:
        cn -= 1

for i in range(1, n):
    for j in range(m - 1):
        res[i][j] = res[i - 1][j + 1] + 1

[print(*i) for i in res]