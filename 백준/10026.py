# 적록색약은 빨간색과 초록색의 차이를 거의 느끼지 못한다. 
# 따라서, 적록색약인 사람이 보는 그림은 아닌 사람이 보는 그림과는 좀 다를 수 있다.
# 크기가 N×N인 그리드의 각 칸에 R(빨강), G(초록), B(파랑) 중 하나를 색칠한 그림이 있다. 
# 그림은 몇 개의 구역으로 나뉘어져 있는데, 구역은 같은 색으로 이루어져 있다. 또, 같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속한다. (색상의 차이를 거의 느끼지 못하는 경우도 같은 색상이라 한다)
# 예를 들어, 그림이 아래와 같은 경우에
# RRRBB
# GGBBB
# BBBRR
# BBRRR
# RRRRR
# 적록색약이 아닌 사람이 봤을 때 구역의 수는 총 4개이다. (빨강 2, 파랑 1, 초록 1) 하지만, 적록색약인 사람은 구역을 3개 볼 수 있다. (빨강-초록 2, 파랑 1)
# 그림이 입력으로 주어졌을 때, 적록색약인 사람이 봤을 때와 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램을 작성하시오.

import sys
    
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):
    visited[x][y] = True
    cur = grid[x][y]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny]==False:
                if grid[nx][ny] == cur:
                    dfs(nx,ny)

n = int(input())
grid = []
grid_gb = []
visited = [[False] * n for _ in range(n)]
cnt = 0 

for _ in range(n):
    temp = input()
    grid.append(list(temp))
    temp = temp.replace('R', 'G')
    grid_gb.append(list(temp))

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

print(cnt, end=' ')
visited = [[False] * n for _ in range(n)]
grid = grid_gb
cnt = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1
print(cnt)