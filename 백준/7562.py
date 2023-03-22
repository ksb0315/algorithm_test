# 체스판 위에 한 나이트가 놓여져 있다. 나이트가 한 번에 이동할 수 있는 칸은 아래 그림에 나와있다. 나이트가 이동하려고 하는 칸이 주어진다. 나이트는 몇 번 움직이면 이 칸으로 이동할 수 있을까?

import sys
from collections import deque

input = sys.stdin.readline

dx = [-2, -2, -1, -1, 1, 1, 2, 2]
dy = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs(x,y, x_end, y_end):
    q = deque()
    q.append([x, y])
    board[x][y] = 1
    while q:
        x, y = q.popleft()
        if x == x_end and y == y_end:
            return board[x][y]-1
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < l and 0 <= ny < l:
                if board[nx][ny] == 0:
                    q.append([nx, ny])
                    board[nx][ny] = board[x][y] + 1

case = int(input())

for _ in range(case):
    l = int(input())
    board = [[0] * (l) for _ in range(l)]
    x1, y1 = map(int, input().split())
    x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(0)
        continue
    ans = bfs(x1, y1, x2, y2)
    print(ans)