# 히스토그램은 직사각형 여러 개가 아래쪽으로 정렬되어 있는 도형이다. 각 직사각형은 같은 너비를 가지고 있지만, 높이는 서로 다를 수도 있다. 예를 들어, 왼쪽 그림은 높이가 2, 1, 4, 5, 1, 3, 3이고 너비가 1인 직사각형으로 이루어진 히스토그램이다.
# 히스토그램에서 가장 넓이가 큰 직사각형을 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

while True:
    hist = list(map(int, input().split()))
    if hist[0] == 0: break
    n = hist[0]    
    hist = hist[1:]
    
    start = 0
    end = n-1
    mid = (start + end) // 2
nnn
