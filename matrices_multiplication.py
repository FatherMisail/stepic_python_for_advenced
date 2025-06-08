'''
 Sample Input 2:
3 2
2 5
6 7
1 8

2 3
1 2 1
0 1 0

Sample Output 2:
2 9 2
6 19 6
1 10 1
'''

n, m = [int(i) for i in input().split()]
M1 = [[int(j) for j in input().split()] for _ in range(n)]

input()
m, k = [int(i) for i in input().split()]
M2 = [[int(j) for j in input().split()] for _ in range(m)]
M3 = [[0] * k for i in range(n)]

for i in range(n):
    for j in range(k):
        for p in range(m):
            M3[i][j] += M1[i][p] * M2[p][j]

for r in M3:
    print(*r)