# 트리(graph)는 사이클이 없는 무방향 그래프이다. 트리에서는 어떤 두 노드를 선택해도 둘 사이에 경로가 항상 하나만 존재하게 된다. 트리에서 어떤 두 노드를 선택해서 양쪽으로 쫙 당길 때, 가장 길게 늘어나는 경우가 있을 것이다. 
# 이럴 때 트리의 모든 노드들은 이 두 노드를 지름의 끝 점으로 하는 원 안에 들어가게 된다.
# 이런 두 노드 사이의 경로의 길이를 트리의 지름이라고 한다. 
# 정확히 정의하자면 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 말한다.
# 입력으로 루트가 있는 트리를 가중치가 있는 간선들로 줄 때, 트리의 지름을 구해서 출력하는 프로그램을 작성하시오. 아래와 같은 트리가 주어진다면 트리의 지름은 45가 된다.
# 트리의 노드는 1부터 n까지 번호가 매겨져 있다.

import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]

def dfs(node, n_len):
    for a, b in graph[node]:
        if dist[a] == -1:
            dist[a] = n_len + b
            dfs(a, n_len + b)

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

dist = [-1] * (n + 1)
dist[1] = 0
dfs(1, 0)

s = dist.index(max(dist))
dist = [-1] * (n + 1)
dist[s] = 0
dfs(s, 0)

print(max(dist))    