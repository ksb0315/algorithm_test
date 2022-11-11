# 2차원 좌표 평면 위에 있는 점 3개 P1, P2, P3가 주어진다. P1, P2, P3를 순서대로 이은 선분이 어떤 방향을 이루고 있는지 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

def ccw(i, j, k):
    # 신발끈 공식을 이용한 삼각형 넓이 구하기
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0]) 
    if area2 > 0:
        return 1
    elif area2 < 0:
        return -1
    else:
        return 0

p1 = list(map(int,input().split()))
p2 = list(map(int,input().split()))
p3 = list(map(int,input().split()))

print(ccw(p1, p2, p3))

