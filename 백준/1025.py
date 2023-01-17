# N행 M열의 표 A가 있고, 표의 각 칸에는 숫자가 하나씩 적혀있다.
# 연두는 서로 다른 1개 이상의 칸을 선택하려고 하는데, 행의 번호가 선택한 순서대로 등차수열을 이루고 있어야 하고, 열의 번호도 선택한 순서대로 등차수열을 이루고 있어야 한다. 이렇게 선택한 칸에 적힌 수를 순서대로 이어붙이면 정수를 하나 만들 수 있다.
# 연두가 만들 수 있는 정수 중에서 가장 큰 완전 제곱수를 구해보자. 완전 제곱수란 어떤 정수를 제곱한 수이다.

import sys
input = sys.stdin.readline

n, m = map(int,input().split())
board = [list(input().strip()) for _ in range(n)]
ans = -1

def sqrt(s):
    s = int(s)
    return int(s ** 0.5) ** 2 == s


for i in range(n):
    for j in range(m): 
        for row_d in range(-n,n):
            for col_d in range(-m,m): 
                s = ""
                x,y = i,j
                if row_d == 0 and col_d == 0:
                    continue
                while 0 <= x <  n and 0 <= y < m:
                    s += board[x][y]
                    if sqrt(s):
                        ans = max(ans,int(s))
                    x += row_d
                    y += col_d
print(ans)