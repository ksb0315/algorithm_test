# 폴리오미노란 크기가 1×1인 정사각형을 여러 개 이어서 붙인 도형이며, 다음과 같은 조건을 만족해야 한다.
# 정사각형은 서로 겹치면 안 된다.
# 도형은 모두 연결되어 있어야 한다.
# 정사각형의 변끼리 연결되어 있어야 한다. 즉, 꼭짓점과 꼭짓점만 맞닿아 있으면 안 된다.
# 아름이는 크기가 N×M인 종이 위에 테트로미노 하나를 놓으려고 한다. 종이는 1×1 크기의 칸으로 나누어져 있으며, 각각의 칸에는 정수가 하나 쓰여 있다.
# 테트로미노 하나를 적절히 놓아서 테트로미노가 놓인 칸에 쓰여 있는 수들의 합을 최대로 하는 프로그램을 작성하시오.
# 테트로미노는 반드시 한 정사각형이 정확히 하나의 칸을 포함하도록 놓아야 하며, 회전이나 대칭을 시켜도 된다.

import sys
input = lambda : sys.stdin.readline()

move = [(-1,0),(1,0),(0,-1),(0,1)]
def dfs(r, c, depth, s):
    global max_value
    if s + maxv*(4-depth) <= max_value:
        return        
    if depth >= 4:
        if max_value < s:
            max_value = s
        return
    else:
        for dr, dc in move:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and visited[nr][nc] == 0:
                if depth == 2:
                    visited[nr][nc] = 1
                    dfs(r, c, depth + 1, s + board[nr][nc])
                    visited[nr][nc] = 0

                visited[nr][nc] = 1
                dfs(nr, nc, depth + 1, s + board[nr][nc])
                visited[nr][nc] = 0


n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

maxv = max(map(max, board))

max_value = 0
visited = [[0]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i,j,1,board[i][j])
        visited[i][j] = 0

print(max_value)