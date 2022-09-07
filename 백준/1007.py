# 평면 상에 N개의 점이 찍혀있고, 그 점을 집합 P라고 하자. 집합 P의 벡터 매칭은 벡터의 집합인데, 모든 벡터는 집합 P의 한 점에서 시작해서, 또 다른 점에서 끝나는 벡터의 집합이다. 또, P에 속하는 모든 점은 한 번씩 쓰여야 한다.
# 벡터 매칭에 있는 벡터의 개수는 P에 있는 점의 절반이다.
# 평면 상의 점이 주어졌을 때, 집합 P의 벡터 매칭에 있는 벡터의 합의 길이의 최솟값을 출력하는 프로그램을 작성하시오.

import sys
import itertools
import math

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    arr = []
    x_total = 0
    y_total = 0
    for _ in range(n):
        x, y = map(int,input().split())
        arr.append([x, y])
        x_total += x
        y_total += y
    
    res = float('inf')
    comp = list(itertools.combinations(arr, n//2))

    for component in comp:
        component = list(component)
        x1_total = 0
        y1_total = 0
        for x1,y1 in component:
            x1_total += x1
            y1_total += y1

        x2_total = x_total - x1_total
        y2_total = y_total - y1_total

        res = min(res, math.sqrt((x1_total - x2_total) ** 2 + (y1_total - y2_total) ** 2))
    
    print(res)