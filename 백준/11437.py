# N(2 ≤ N ≤ 50,000)개의 정점으로 이루어진 트리가 주어진다. 트리의 각 정점은 1번부터 N번까지 번호가 매겨져 있으며, 루트는 1번이다.
# 두 노드의 쌍 M(1 ≤ M ≤ 10,000)개가 주어졌을 때, 두 노드의 가장 가까운 공통 조상이 몇 번인지 출력한다.

from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
tree  = [[]for _ in range(n+1)]
depth = [0] * (n+1)
parant = [0] * (n+1)
visited = [False] * (n+1)
for _ in range(n-1):
    s,e = map(int, input().split())
    tree[s].append(e)
    tree[e].append(s)

def bfs(s):
    queue = deque()
    queue.append(s)
    while queue:
        node = queue.popleft()
        visited[node] = True
        for i in tree[node]:
            if not visited[i]:
                depth[i] = depth[node] + 1
                parant[i] = node
                queue.append(i)

def LCA(a,b):
    if depth[a] < depth[b]:
        temp = a
        a=b
        b=temp
    diff = depth[a] - depth[b]
    for _ in range(diff):
        a = parant[a]
    while a!=b:
        a = parant[a]
        b = parant[b]
    return a

bfs(1)

m = int(input())
for _ in range(m):
    a,b = map(int, input().split())
    print(LCA(a, b))

## 실패