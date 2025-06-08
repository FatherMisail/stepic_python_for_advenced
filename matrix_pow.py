n = int(input())
M1 = [[int(j) for j in input().split()] for _ in range(n)]
m = int(input())
M2 = [row.copy() for row in M1]
M3 = [[0] * n for i in range(n)]

for _ in range(m - 1):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                M3[i][j] += M1[i][k] * M2[k][j]
    for i in range(n):
        for j in range(n):
            M1[i][j] = M3[i][j]
            M3[i][j] = 0

for r in M1:
    print(*r)
