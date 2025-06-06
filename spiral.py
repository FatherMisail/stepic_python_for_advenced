# n, m = 1, 1
n, m = [int(i) for i in input().split()]
M = [[0 for j in range(m)] for i in range(n)]

i = 0
j = 0
first_time = True
k = 1
mxk = m * n
while True:
    if k == mxk:
        break
    m -= 1
    for _ in range(m):
        M[i][j] = k
        k += 1
        j += 1

    if k == mxk:
        break
    n -= 1
    for _ in range(n):
        M[i][j] = k
        k += 1
        i += 1

    if k == mxk:
        break
    if not first_time:
        m -= 1
    for _ in range(m):
        M[i][j] = k
        k += 1
        j -= 1

    if k == mxk:
        break
    n -= 1
    for _ in range(n):
        M[i][j] = k
        k += 1
        i -= 1

    first_time = False

M[i][j] = k

for r in M:
    for c in r:
        print(str(c).ljust(3), end=' ')
    print()
