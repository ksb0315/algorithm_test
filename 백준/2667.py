# <그림 1>과 같이 정사각형 모양의 지도가 있다. 1은 집이 있는 곳을, 0은 집이 없는 곳을 나타낸다. 철수는 이 지도를 가지고 연결된 집의 모임인 단지를 정의하고, 단지에 번호를 붙이려 한다. 
# 여기서 연결되었다는 것은 어떤 집이 좌우, 혹은 아래위로 다른 집이 있는 경우를 말한다. 대각선상에 집이 있는 경우는 연결된 것이 아니다. <그림 2>는 <그림 1>을 단지별로 번호를 붙인 것이다. 지도를 입력하여 단지수를 출력하고, 각 단지에 속하는 집의 수를 오름차순으로 정렬하여 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
apart = []
ans = []
cnt = 0 
res = 0
for _ in range(n):
    apart.append(list(map(int,input().rstrip())))
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(x,y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False
    if apart[x][y] == 1:
        global cnt
        cnt += 1
        apart[x][y] = 0
        for i in range(4):
            dfs(x + dx[i], y + dy[i])
        return True

for i in range(n):   
    for j in range(n):
        if dfs(i, j):
            ans.append(cnt)
            res += 1
            cnt = 0
        
ans.sort()
print(res)
for i in range(len(ans)):
    print(ans[i])