# 그래프가 주어졌을 때, 그 그래프의 최소 스패닝 트리를 구하는 프로그램을 작성하시오.
# 최소 스패닝 트리는, 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리를 말한다.

import sys
import heapq

input = sys.stdin.readline
 
v, e = map(int, input().split())
visited = [False]*(v+1)
elist = [[] for _ in range(v+1)]
heap = [[0, 1]]
for _ in range(e):
    s, e, w = map(int, input().split())
    elist[s].append([w, e])
    elist[e].append([w, s])
 
ans = 0
cnt = 0
while heap:
    if cnt == v:
        break
    w, s = heapq.heappop(heap)
    if not visited[s]:
        visited[s] = True
        ans += w
        cnt += 1
        for i in elist[s]:
            heapq.heappush(heap, i)
 
print(ans)
