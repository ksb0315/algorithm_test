# 크리스마스에는 산타가 착한 아이들에게 선물을 나눠준다. 
# 올해도 산타는 선물을 나눠주기 위해 많은 노력을 하고 있는데, 전세계를 돌아댕기며 착한 아이들에게 선물을 나눠줄 것이다. 
# 하지만 산타의 썰매는 그렇게 크지 않기 때문에, 세계 곳곳에 거점들을 세워 그 곳을 방문하며 선물을 충전해 나갈 것이다. 
# 또한, 착한 아이들을 만날 때마다 자신이 들고있는 가장 가치가 큰 선물 하나를 선물해 줄 것이다.
# 이제 산타가 선물을 나눠줄 것이다. 차례대로 방문한 아이들과 거점지의 정보들이 주어졌을 때, 아이들이 준 선물들의 가치들을 출력하시오. 만약 아이들에게 줄 선물이 없다면 -1을 출력하시오.

import sys
import heapq

input = sys.stdin.readline

n = int(input())
gifts = []

for _ in range(n):
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        if gifts:
            gift = -heapq.heappop(gifts)
        else:
            gift = -1
        print(gift)
    else:
        for i in range(1, arr[0]+1):
            heapq.heappush(gifts, -arr[i])
    