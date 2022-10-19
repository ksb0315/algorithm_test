# N×M크기의 배열로 표현되는 미로가 있다.
# 1	 0  1  1  1  1
# 1  0	1  0  1	 0
# 1	 0  1  0  1	 1
# 1  1  1  0  1	 1
# 미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.
# 위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())
maze = []
cnt = 0

for _ in range(n):
    maze.append(list(map(int, input().rstrip())))

def bfs(x, y):
    dx = [-1, 1, 0, 0] 
    dy = [0, 0, -1, 1]
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(4):
            x_new = x + dx[i]
            y_new = y + dy[i]
            if x_new < 0 or x_new >= n or y_new < 0 or y_new >= m:
                continue    
            elif maze[x_new][y_new] == 0:
                continue
            elif maze[x_new][y_new] == 1:
                maze[x_new][y_new] = maze[x][y] + 1
                q.append((x_new, y_new))
    return maze[n-1][m-1]

print(bfs(0, 0))