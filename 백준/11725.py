# 루트 없는 트리가 주어진다. 이때, 트리의 루트를 1이라고 정했을 때, 각 노드의 부모를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)
for _ in range(n-1):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def dfs(n):
    for i in graph[n]:
        if parent[i] == 0:
            parent[i] = n
            dfs(i)
            
dfs(1)
for i in range(2,n+1):
    print(parent[i])
