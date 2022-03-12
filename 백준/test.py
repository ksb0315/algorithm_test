import sys
import heapq

n = int(sys.stdin.readline())
heap = []
ans = []
for _ in range(n):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            ans.append(heapq.heappop(heap))
        except:
            ans.append(0)

for a in ans:
    print(a)