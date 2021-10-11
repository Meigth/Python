n, m = [int(i) for i in input().split()]
res = []
res += [[i + 1 for i in range(m)]]
res += [[0] * m for i in range(n - 1)]
cnt = 0
ind = True

while 0 in res[n // 2]:
    if ind:
        for i in range(cnt + 1, n - cnt):
            res[i][-cnt - 1] = res[i - 1][-cnt - 1] + 1
        for i in range(m - cnt - 2, cnt - 1, -1):
            res[-cnt - 1][i] = res[-cnt - 1][i + 1] + 1
        ind = not(ind)
    else:
        for i in range(n - cnt - 2, cnt, -1):
            res[i][cnt] = res[i + 1][cnt] + 1
        for i in range(cnt + 1, m - cnt - 1):
            res[cnt + 1][i] = res[cnt + 1][i - 1] + 1
        ind = not(ind)
        cnt += 1

[print(*i, sep='  ') for i in res]