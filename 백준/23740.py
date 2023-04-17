# 서강 나라에서는 일직선 도로를 따라 
# $N$개의 버스 노선을 운영 중이다. 필요할 때마다 노선을 새로 만든 탓에 겹치거나 중복되는 노선이 많다. 복잡한 버스 노선에 지친 시민들을 위해 버스 노선을 개편하기로 했다.
# 각 버스 노선은 세 정수 $S$, $E$, $C$로 나타낼 수 있으며, 구간 $[S,E]$를 요금 $C$로 운행한다는 뜻이다. 
# 어떤 두 버스 노선의 구간이 한 점 이상에서 겹친다면, 두 구간을 합친 새 노선으로 대체한다. 이때 요금은 더 낮은 금액의 요금을 따르기로 했다. 버스 노선 개편은 구간이 겹치는 버스 노선이 없을 때까지 진행한다.
# 그림 D.1: 개편 전과 개편 후의 버스 노선도
# 버스 노선들의 정보가 주어지면, 개편이 끝난 후 버스 노선의 정보를 출력하는 프로그램을 작성하자.

import sys

input =sys.stdin.readline

n = int(input())

bus = []
for _ in range(n):
    bus.append(list(map(int, input().split())))

bus.sort(key=lambda x: x[1])
bus.sort(key=lambda x: x[0])

ans = []
flag = False

left = bus[0][0]
right = bus[0][1]
min_cost = bus[0][2]

for i in range(1, len(bus)):
    start, end, cost = bus[i]
    if start <= right: # 겹칠때
        if end > right:
            right = end
        if min_cost > cost:
            min_cost = cost
    else: # 안겹칠때
        ans.append([left, right, min_cost])
        left = start
        right = end 
        min_cost = cost

ans.append([left, right, min_cost])
print(len(ans))
for a in ans:
    print(*a)
