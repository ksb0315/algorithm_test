# 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
axes = []
for _ in range(n):
    axes.append(list(map(int, input().split())))

axes.sort(key=lambda x: x[0])
axes.sort(key=lambda x: x[1])

print(axes)