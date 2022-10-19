# 도현이는 우주의 신이다. 이제 도현이는 아무렇게나 널브러져 있는 n개의 별들을 이어서 별자리를 하나 만들 것이다. 별자리의 조건은 다음과 같다.
# 별자리를 이루는 선은 서로 다른 두 별을 일직선으로 이은 형태이다.
# 모든 별들은 별자리 위의 선을 통해 서로 직/간접적으로 이어져 있어야 한다.
# 별들이 2차원 평면 위에 놓여 있다. 선을 하나 이을 때마다 두 별 사이의 거리만큼의 비용이 든다고 할 때, 별자리를 만드는 최소 비용을 구하시오.
import sys
import math

input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
parent = [i for i in range(n + 1)]

stars = []
edges = []
result = 0

for _ in range(n):
    x, y = map(float, input().split())
    stars.append((x, y))

for i in range(n - 1):
    for j in range(i + 1, n):
        edges.append((math.sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2), i, j))

edges.sort()

for edge in edges:
    cost, x, y = edge

    if find_parent(x) != find_parent(y):
        union_parent(x, y)
        result += cost

print(round(result, 2))