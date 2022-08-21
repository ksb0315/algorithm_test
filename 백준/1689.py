# 1차원 좌표계 위에 선분 N개가 있다. 선분이 최대로 겹쳐있는 부분의 겹친 선분의 개수를 구해보자. 선분의 끝 점에서 겹치는 것은 겹치는 것으로 세지 않는다.

import sys
import heapq

input = sys.stdin.readline

n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]

array.sort(key=lambda x:x[0])
min_heap = []
heapq.heappush(min_heap, array[0][1])
result = 1

for x in array[1:]:
    while min_heap and min_heap[0] <= x[0]:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, x[1])
    result = max(result, len(min_heap))

print(result)