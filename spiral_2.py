n, m = 9, 8
# n, m = [int(i) for i in input().split()]
M = [[0] * m for i in range(n)]

i, j, k = 0, 0, 1
di, dj = 0, 1
while k < m * n:
    while i + di < n and j + dj < m and M[i + di][j + dj] == 0:
        M[i][j] = k
        k += 1
        i += di
        j += dj

    di, dj = dj, -di

M[i][j] = k

for r in M:
    for c in r:
        print(str(c).ljust(3), end=' ')
    print()
