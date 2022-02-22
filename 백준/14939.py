# 전구 100개가 10×10 정사각형 모양으로 늘어서 있다. 전구에 달린 스위치를 누르면 그 전구와 위, 아래, 왼쪽, 오른쪽에 있는 전구의 상태도 바뀐다. 전구 100개의 상태가 주어지면 모든 전구를 끄기 위해 최소한으로 눌러야 하는 스위치의 개수를 출력하라

table = []
for i in range(10):
    temp = list(input())
    for j in range(10):
        if temp[j] == 'O':
            temp[j] = True
            continue
        temp[j] = False 
    table.append(temp)
 
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, 0, -1, 1]
ans = 101
for f in range(1<<10):
    a = []
    for i in range(10):
        a.append(table[i][:])
    cnt = 0
 
    for i in range(10):
        if f & (1<<i): 
            cnt += 1
            for k in range(5):
                nx = i + dx[k]
                ny = 0 + dy[k]
                if 0 <= nx <= 9 and 0 <= ny <= 9:
                    a[ny][nx] = not a[ny][nx]
 
    for i in range(1, 10): 
        for j in range(10): 
            if not a[i-1][j]: 
                continue
            for k in range(5):
                nx = j + dx[k]
                ny = i + dy[k]
                if 0 <= nx <= 9 and 0 <= ny <= 9:
                    a[ny][nx] = not a[ny][nx]
            cnt += 1
 
 
    can = True
    for i in range(10):
        if a[9][i] == True:
            can = False
 
    if can:
        ans = min(cnt, ans)
 
print(ans if ans != 101 else -1)