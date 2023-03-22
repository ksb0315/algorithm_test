# 2차원 배열이 주어졌을 때 (i, j) 위치부터 (x, y) 위치까지에 저장되어 있는 수들의 합을 구하는 프로그램을 작성하시오. 배열의 (i, j) 위치는 i행 j열을 나타낸다.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(map(int, input().split())))

k = int(input())
ans = []

for _ in range(k):
    res = 0
    i, j, x, y = map(int, input().split())
    for l in range(i-1,x):
        res += sum(mat[l][j-1:y])
    ans.append(res)

for a in ans:
    print(a)

