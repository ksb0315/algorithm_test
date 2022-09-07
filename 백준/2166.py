# 2차원 평면상에 N(3 ≤ N ≤ 10,000)개의 점으로 이루어진 다각형이 있다. 이 다각형의 면적을 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
area = 0
axis = []

for _ in range(n):
    axis.append(list(map(int,input().split())))
axis.append(axis[0])

for i in range(n):
    area += (axis[i][0] * axis[i+1][1]) - (axis[i+1][0] * axis[i][1])

print(round(abs(area) / 2, 1))
