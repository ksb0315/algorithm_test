# 성경이는 트럭을 정글 속에서 운전하다가 트럭의 연료탱크에 갑자기 구멍이 나서 1km를 가는데 1L의 연료가 새 나가게 되었다. 
# 이것을 고치기 위해서는 가장 가까운 마을에 가야 한다. 그런데 그냥 가다가는 중간에 연료가 다 빠질 수가 있다. 
# 다행스럽게도 정글 곳곳에 연료를 채울 수 있는 주유소가 N개 있다. 
# 그런데 정글 속에서 중간에 차를 멈추는 행위는 매우 위험한 행위이므로 주유소에서 멈추는 횟수를 최소화 하려 한다.
# 그리고 다행이도 성경이의 트럭은 매우 좋아서 연료 탱크에는 연료의 제한이 없이 많이 충분히 많이 넣을 수 있다고 한다. 각각의 주유소의 위치와, 각 주유소에서 얻을 수 있는 연료의 양이 주어져 있을 때, 주유소에서 멈추는 횟수를 구하는 프로그램을 작성하시오.
# 정글은 일직선이고, 성경이의 트럭과 주유소도 모두 일직선 위에 있다. 주유소는 모두 성경이의 트럭을 기준으로 오른쪽에 있다.
import sys
import heapq

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
arrive, fuel = map(int, input().split())
ans = 0
info.append([arrive, 0])
info.sort()
heap = []

for i in range(len(info)):
    if fuel < info[i][0]:
        while heap:
            fuel += -heapq.heappop(heap)
            ans += 1
            if fuel >= info[i][0]:
                break
    if (not heap) and fuel < info[i][0]:
        ans = -1
        break
    else:
        heapq.heappush(heap, -info[i][1])

print(ans)