# 2차원 좌표 평면 위의 두 선분 L1, L2가 주어졌을 때, 두 선분이 교차하는지 아닌지 구해보자. 한 선분의 끝 점이 다른 선분이나 끝 점 위에 있는 것도 교차하는 것이다.
# L1의 양 끝 점은 (x1, y1), (x2, y2), L2의 양 끝 점은 (x3, y3), (x4, y4)이다.
import sys

input = sys.stdin.readline

def ccw(i, j, k):
    # 신발끈 공식을 이용한 삼각형 넓이 구하기 이용
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0]) 
    if area2 > 0:
        return 1
    elif area2 < 0:
        return -1
    else:
        return 0

l1_s1, l1_s2, l1_e1, l1_e2 = map(int, input().split())
l2_s1, l2_s2, l2_e1, l2_e2 = map(int, input().split())
a1 = [l1_s1, l1_s2]
a2 = [l1_e1, l1_e2]
b1 = [l2_s1, l2_s2]
b2 = [l2_e1, l2_e2]

if ccw(a1,a2,b1)*ccw(a1,a2,b2) <= 0 and ccw(b1,b2,a1)*ccw(b1,b2,a2) <= 0:
    if ccw(a1,a2,b1)*ccw(a1,a2,b2) == 0 and ccw(b1,b2,a1)*ccw(b1,b2,a2) == 0:
        if (max(a1[0],a2[0]) >= min(b1[0],b2[0]) and max(b1[0],b2[0]) >= min(a1[0],a2[0])) and (max(a1[1],a2[1]) >= min(b1[1],b2[1]) and max(b1[1],b2[1]) >= min(a1[1],a2[1])):
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)

