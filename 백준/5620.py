# 평면상에 n개의 점 (P1, .... ,  Pn) 이 놓여져있다고 했을 때, 거리가 최소인 두 개의 점을 구하고 그 거리를 알고 싶다.

import sys

input = sys.stdin.readline

n = int(input())
points = []

for _ in range(n):
    points.append(list(map(int, input().split())))
points.sort()

def getDist(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1]-p2[1]) ** 2

def compare(left, right):
    if left == right:
        return float('inf')
    if right - left == 1:
        return getDist(points[left], points[right])
    
    mid = (left + right) // 2
    mdist = min(compare(left, mid), compare(mid, right))
    res = []
    for i in range(left, right+1):
        if (points[mid][0] - points[i][1]) ** 2 < mdist:
            res.append(points[i])
    res.sort(key=lambda x:x[1])

    for i in range(len(res) - 1):
        for j in range(i+1, len(res)):
            if (res[i][1] - res[j][1]) ** 2 < mdist:
                mdist = min(mdist, getDist(res[i], res[j]))
            else:
                break

    return mdist

print(compare(0, n-1))