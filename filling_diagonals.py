# n, m = 32, 12
n, m = [int(i) for i in input().split()]
M = [[0 for _ in range(m)] for _ in range(n)]

frame = 0
i_fr_shift = 0
j_fr_shift = 0
i = 0
j = 0
k = 1
while k <= m*n:
    if frame + i_fr_shift < n and frame + j_fr_shift < m:
        frame += 1
    elif frame + i_fr_shift == n and frame + j_fr_shift == m:
        frame -= 1
        i_fr_shift += 1
        j_fr_shift += 1
    elif frame + i_fr_shift == n:
        j_fr_shift += 1
    elif frame + j_fr_shift == m:
        i_fr_shift += 1

    for i in range(frame):
        p = i_fr_shift + i
        q = j_fr_shift + frame - 1 - i
        M[p][q] = k
        k += 1

for r in M:
    print(*r)
print()
