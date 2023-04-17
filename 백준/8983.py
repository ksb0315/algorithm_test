# KOI 사냥터에는 N 마리의 동물들이 각각 특정한 위치에 살고 있다. 
# 사냥터에 온 사냥꾼은 일직선 상에 위치한 M 개의 사대(총을 쏘는 장소)에서만 사격이 가능하다. 편의상, 일직선을 x-축이라 가정하고, 사대의 위치 x1, x2, ..., xM은 x-좌표 값이라고 하자. 
# 각 동물이 사는 위치는 (a1, b1), (a2, b2), ..., (aN, bN)과 같이 x,y-좌표 값으로 표시하자. 
# 동물의 위치를 나타내는 모든 좌표 값은 양의 정수이다.
# 사냥꾼이 가지고 있는 총의 사정거리가 L이라고 하면, 사냥꾼은 한 사대에서 거리가 L 보다 작거나 같은 위치의 동물들을 잡을 수 있다고 한다. 단, 사대의 위치 xi와 동물의 위치 (aj, bj) 간의 거리는 |xi-aj| + bj로 계산한다.
# 예를 들어, 아래의 그림과 같은 사냥터를 생각해 보자. (사대는 작은 사각형으로, 동물의 위치는 작은 원으로 표시되어 있다.) 사정거리 L이 4라고 하면, 점선으로 표시된 영역은 왼쪽에서 세 번째 사대에서 사냥이 가능한 영역이다.
# 사대의 위치와 동물들의 위치가 주어졌을 때, 잡을 수 있는 동물의 수를 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
spots = list(map(int, input().split()))
spots.sort()
animals = [list(map(int, input().split())) for i in range(n)]

cnt = 0
for a,b in animals:
    start = 0
    end = len(spots)-1
    while start<end:
        mid = (start+end)//2
        if spots[mid] < a:
            start = mid+1
        else:
            end = mid
    if abs(spots[end]-a)+b<=l or abs(spots[end-1]-a)+b<=l:
        cnt += 1

print(cnt)