# 차세대 영농인 한나는 강원도 고랭지에서 유기농 배추를 재배하기로 하였다. 
# 농약을 쓰지 않고 배추를 재배하려면 배추를 해충으로부터 보호하는 것이 중요하기 때문에, 한나는 해충 방지에 효과적인 배추흰지렁이를 구입하기로 결심한다. 이 지렁이는 배추근처에 서식하며 해충을 잡아 먹음으로써 배추를 보호한다. 
# 특히, 어떤 배추에 배추흰지렁이가 한 마리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 그 배추들 역시 해충으로부터 보호받을 수 있다. 
# 한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것이다.
# 한나가 배추를 재배하는 땅은 고르지 못해서 배추를 군데군데 심어 놓았다. 
# 배추들이 모여있는 곳에는 배추흰지렁이가 한 마리만 있으면 되므로 서로 인접해있는 배추들이 몇 군데에 퍼져있는지 조사하면 총 몇 마리의 지렁이가 필요한지 알 수 있다. 예를 들어 배추밭이 아래와 같이 구성되어 있으면 최소 5마리의 배추흰지렁이가 필요하다. 
# 0은 배추가 심어져 있지 않은 땅이고, 1은 배추가 심어져 있는 땅을 나타낸다.

import sys
from collections import deque

input = sys.stdin.readline

dx = [0,0,1,-1]
dy = [1,-1,0,0]

case = int(input())

def bfs(farm, a, b):
    queue = deque()
    queue.append((a,b))
    farm[a][b] = 0

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >=n or ny < 0 or ny >= m:
                continue
            if farm[nx][ny] == 1:
                farm[nx][ny] = 0
                queue.append((nx, ny))
    return

for _ in range(case):
    cnt = 0
    n, m, k = map(int,input().split())
    farm = [[0]*m for _ in range(n)]

    for j in range(k):
        x, y = map(int, input().split())
        farm[x][y] = 1

    for a in range(n):
        for b in range(m):
            if farm[a][b] == 1:
                bfs(farm, a, b)
                cnt += 1
    print(cnt)