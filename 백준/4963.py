# 정사각형으로 이루어져 있는 섬과 바다 지도가 주어진다. 섬의 개수를 세는 프로그램을 작성하시오.
# 한 정사각형과 가로, 세로 또는 대각선으로 연결되어 있는 사각형은 걸어갈 수 있는 사각형이다. 
# 두 정사각형이 같은 섬에 있으려면, 한 정사각형에서 다른 정사각형으로 걸어서 갈 수 있는 경로가 있어야 한다. 
# 지도는 바다로 둘러싸여 있으며, 지도 밖으로 나갈 수 없다.

import sys
from collections import deque
input = sys.stdin.readline

dx = [0,0,1,-1,1,-1,1,-1]
dy = [1,-1,0,0,1,1,-1,-1]

def bfs(x, y):
    queue = deque()
    queue.append([x,y])
    graph[y][x] = 0
    
    while queue:
        x, y = queue.popleft()
        for i in range(8):
            next_x = x + dx[i]
            next_y = y + dy[i]
            
            if 0 <= next_x < w and 0 <= next_y < h: 
                if graph[next_y][next_x] == 1:
                    queue.append([next_x, next_y])
                    graph[next_y][next_x] = 0

while(True):
    graph = list()
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    cnt = 0 
    for i in range(h):
        graph.append(list(map(int, input().split())))

    for i in range(h): 
        for j in range(w):
            if graph[i][j] == 1:
                bfs(j, i)
                cnt += 1
    print(cnt)