# 세계적인 도둑 상덕이는 보석점을 털기로 결심했다.
# 상덕이가 털 보석점에는 보석이 총 N개 있다. 각 보석은 무게 Mi와 가격 Vi를 가지고 있다. 
# 상덕이는 가방을 K개 가지고 있고, 각 가방에 담을 수 있는 최대 무게는 Ci이다. 가방에는 최대 한 개의 보석만 넣을 수 있다.
# 상덕이가 훔칠 수 있는 보석의 최대 가격을 구하는 프로그램을 작성하시오.

import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jul = []
for _ in range(n):
    heapq.heappush(jul, list(map(int, sys.stdin.readline().split())))
bags = []
for _ in range(k):
    bags.append(int(sys.stdin.readline()))
bags.sort()
ans = 0
temp = []
for bag in bags:
    while jul and bag >= jul[0][0]:
        heapq.heappush(temp, -heapq.heappop(jul)[1])
    if temp:
        ans -= heapq.heappop(temp)
    elif not jul:
        break
print(ans)
