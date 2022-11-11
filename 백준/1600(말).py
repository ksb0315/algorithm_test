# 동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 그 녀석은 말(Horse)이 되기를 간절히 원했다. 그래서 그는 말의 움직임을 유심히 살펴보고 그대로 따라 하기로 하였다. 말은 말이다. 말은 격자판에서 체스의 나이트와 같은 이동방식을 가진다. 다음 그림에 말의 이동방법이 나타나있다. x표시한 곳으로 말이 갈 수 있다는 뜻이다. 참고로 말은 장애물을 뛰어넘을 수 있다.
# 근데 원숭이는 한 가지 착각하고 있는 것이 있다. 말은 저렇게 움직일 수 있지만 원숭이는 능력이 부족해서 총 K번만 위와 같이 움직일 수 있고, 그 외에는 그냥 인접한 칸으로만 움직일 수 있다. 대각선 방향은 인접한 칸에 포함되지 않는다.
# 이제 원숭이는 머나먼 여행길을 떠난다. 격자판의 맨 왼쪽 위에서 시작해서 맨 오른쪽 아래까지 가야한다. 인접한 네 방향으로 한 번 움직이는 것, 말의 움직임으로 한 번 움직이는 것, 모두 한 번의 동작으로 친다. 격자판이 주어졌을 때, 원숭이가 최소한의 동작으로 시작지점에서 도착지점까지 갈 수 있는 방법을 알아내는 프로그램을 작성하시오.

from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
dx_horse = [-2, -1, 1, 2, 2, 1, -1, -2]
dy_horse = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs():
    q = deque()
    q.append((0, 0, k))
    visit = [[[0 for i in range(31)] for i in range(w)] for i in range(h)]
    while q:
        x, y, z = q.popleft()
        if x == h - 1 and y == w - 1: return visit[x][y][z]
        for i in range(4):
            cur_x = x + dx[i]
            cur_y = y + dy[i]
            if 0 <= cur_x < h and 0 <= cur_y < w and board[cur_x][cur_y] != 1 and visit[cur_x][cur_y][z] == 0:
                visit[cur_x][cur_y][z] = visit[x][y][z] + 1
                q.append((cur_x, cur_y, z))
        if z > 0:
            for i in range(8):
                cur_x = x + dx_horse[i]
                cur_y = y + dy_horse[i]
                if 0 <= cur_x < h and 0 <= cur_y < w and board[cur_x][cur_y] != 1 and visit[cur_x][cur_y][z - 1] == 0:
                    visit[cur_x][cur_y][z - 1] = visit[x][y][z] + 1
                    q.append((cur_x, cur_y, z - 1))
    return -1

k = int(input())
w, h = map(int,input().split())
board = []
for _ in range(h):
    board.append(list(map(int, input().split())))

print(bfs())