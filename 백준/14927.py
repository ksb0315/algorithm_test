# 홍익이는 N x N 전구 판을 가지고 있다. 전구 판에는 각 칸마다 전구가 하나씩 연결되어 있다. 이 전구 판에서 하나의 전구를 누르면, 해당 전구를 포함하여 상하좌우의 총 5개 전구들의 상태가 변화한다. 다시 말해, 5개의 전구들 중 불이 켜져 있던 전구는 불이 꺼지고, 불이 꺼져 있던 전구는 불이 켜진다.
# 홍익이는 현재 전구 판의 상태를 보고 최대한 적은 횟수로 전구들을 눌러 전구판의 모든 전구를 끄고 싶다.
# 홍익이를 도와서 전구 판의 모든 전구를 끌 수 있는 최소 횟수 B를 알아보자.
# 만약, 전구를 끌 수 있는 방법이 없다면, -1을 출력하도록 한다.

import sys
input = sys.stdin.readline
 
n = int(input())
table = []
for i in range(n):
    temp = list(map(int, input().split()))
    table.append(temp)

dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 0, -1, 1]
ans = 2**n+1
for f in range(1<<n):
    a=[]
    for i in range(n):
        a.append(table[i][:])
    cnt = 0
 
    for i in range(n):
        if f & (1<<i):
            cnt += 1
            for k in range(5):
                nx = i + dx[k]
                ny = 0 + dy[k]
                if 0 <= nx < n and 0 <= ny < n:
                    a[ny][nx] = not a[ny][nx]
 
    for i in range(1, n):
        for j in range(n):
            if a[i-1][j]:
                for k in range(5):
                    nx = j + dx[k]
                    ny = i + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        a[ny][nx] = not a[ny][nx]
                cnt += 1
 
    can = True
    for i in range(n):
        if a[-1][i] == True:
            can = False
            break
 
    if can:
        ans = min(cnt, ans)
 
print(ans if ans != 2**n+1 else -1)