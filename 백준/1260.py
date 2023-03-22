# 그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

import sys
from collections import deque
from itertools import combinations, permutations

input = sys.stdin.readline

def bfs(v):
    q=deque([v])
    visit[v]=True
    while q:
        now=q.popleft()
        print(now,end=' ')
        for i in graph[now]:
            if not visit[i]:
                q.append(i)
                visit[i]=True

def dfs(v):
    print(v,end=' ')
    visit[v]=True
    for i in graph[v]:
        if not visit[i]:
            dfs(i)
            visit[i]=True

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [False for _ in range(n+1)]
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in range(len(graph)):
    graph[i].sort()

dfs(v)
print()
visit = [False for _ in range(n+1)]
bfs(v)

