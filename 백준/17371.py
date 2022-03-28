# 혜아는 답답한 3차원 세계를 벗어나 자유로운 2차원 좌표계 위로 집을 옮길 계획이다. 이 좌표계에는 그 어떤 위치에도 주거할 수 있는 시설이 있기 때문에 혜아는 두 실수 Hx, Hy 를 골라 좌표 (Hx, Hy)로 이사할 것이다.
# 이사할 집의 위치를 결정하기 위해 절대적으로 중요한 것은 편의시설이 집으로부터 얼마나 멀리 떨어져 있느냐는 점이다. 좌표계에는 N개의 편의시설이 있는데, 좌표계의 주거지역 정책에 따라 x, y 좌표가 모두 정수인 곳에만 편의시설이 있다.
# 혜아는 N개의 편의시설로 이동하는 데 드는 거리의 평균값이 최소가 되는 좌표로 이사를 가고 싶었지만, 이런 좌표를 찾는 것이 너무 어렵다는 것을 깨달았다. 
# 그래서 그나마 좌표를 찾기 쉽도록 가장 가까운 편의시설까지의 거리와 가장 먼 편의시설까지의 거리의 평균이 최소가 되는 좌표로 이사하려고 한다. 
# 이 좌표계에서 거리는 유클리드 거리를 사용하여, 두 좌표 (Ax, Ay)와 (Bx, By) 사이의 거리는 $\sqrt{(A_x-B_x)^2+(A_y-B_y)^2}$으로 나타난다고 할 때, 혜아를 도와 가능한 위치 중 하나를 구해 주는 프로그램을 작성해보자.

import math

n = int(input())
dist = []
def distance(a1, a2, b1, b2):
    return math.sqrt((a1-b1)**2 + (a2-b2)**2)
for _ in range(n):
    x, y = map(int, input().split())
    dist.append([x, y])
max_d = float('inf')

for i in range(n):
    temp = []
    for j in range(n):
        temp.append(distance(dist[i][0],dist[i][1],dist[j][0],dist[j][1]))
    if max_d > max(temp):
        max_d = max(temp)
        pos = dist[i]
for home in pos:
    print(home, end=' ')