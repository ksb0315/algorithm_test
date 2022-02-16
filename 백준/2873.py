# 상근이는 우리나라에서 가장 유명한 놀이 공원을 운영하고 있다. 이 놀이 공원은 야외에 있고, 다양한 롤러코스터가 많이 있다.
# 어느 날 벤치에 앉아있던 상근이는 커다란 황금을 발견한 기분이 들었다. 자신의 눈 앞에 보이는 이 부지를 구매해서 롤러코스터를 만든다면, 세상에서 가장 재미있는 롤러코스터를 만들 수 있다고 생각했다.
# 이 부지는 직사각형 모양이고, 상근이는 R행 C열의 표 모양으로 나누었다. 롤러코스터는 가장 왼쪽 위 칸에서 시작할 것이고, 가장 오른쪽 아래 칸에서 도착할 것이다. 롤러코스터는 현재 있는 칸과 위, 아래, 왼쪽, 오른쪽으로 인접한 칸으로 이동할 수 있다. 각 칸은 한 번 방문할 수 있고, 방문하지 않은 칸이 있어도 된다.
# 각 칸에는 그 칸을 지나갈 때, 탑승자가 얻을 수 있는 기쁨을 나타낸 숫자가 적혀있다. 롤러코스터를 탄 사람이 얻을 수 있는 기쁨은 지나간 칸의 기쁨의 합이다. 가장 큰 기쁨을 주는 롤러코스터는 어떻게 움직여야 하는지를 구하는 프로그램을 작성하시오.

import sys

c, r = map(int, sys.stdin.readline().split()) #열, 행

lr = [] #직사각형 행복지수
for i in range(r):
    lc = list(map(int, sys.stdin.readline().split())) #행 별 행복지수
    lr.append(lc)
min_list = []
if r % 2 == 1:
    print(('R' * (c-1) + 'D' + 'L' * (c-1) + 'D') * (r//2) + 'R' * (c-1))
elif c % 2 == 1:
    print(('R' * (r-1) + 'D' + 'L' * (r-1) + 'D') * (c//2) + 'R' * (r-1))
elif r % 2 == 0 and c % 2 == 0: # 건너뛸 장소 찾기
    low = 1000
    position = [-1, -1]
    for i in range(r):
        if i % 2 == 0:
            for j in range(1, c, 2):
                if low > lr[i][j]:
                    low = lr[i][j]
                    position = [i, j]
        else: # i % 2 == 1
            for j in range(0, c, 2):
                if low > lr[i][j]:
                    low = lr[i][j]
                    position = [i, j]
    res = ('D'*(r-1) + 'R' + 'U'*(r-1) + 'R')*(position[1]//2)
    x = 2 * (position[1]//2)
    y = 0
    xbound = 2 * (position[1]//2) + 1
    while x != xbound or y != r - 1:
        if x < xbound and [y, xbound] != position:
            x += 1
            res += 'R'
        elif x == xbound and [y, xbound-1] != position:
            x -= 1
            res += 'L'
        if y != r-1:
            y += 1
            res += 'D'
 
    res += ('R' + 'U'*(r-1) + 'R' + 'D'*(r-1))*((c-position[1]-1)//2)
 
    print(res)
