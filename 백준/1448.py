# 세준이는 N개의 빨대를 가지고 있다. N개의 빨대 중에 3개의 빨대를 선택했을 때, 이 빨대로 삼각형을 만들 수 있다면, 세 변의 길이의 합의 최댓값을 구하고 싶다.

import sys
input = sys.stdin.readline

N = int(input())

straw=[]
for _ in range(N):
    straw.append(int(input()))

straw.sort(reverse=True)

res=0
for i in range(len(straw)-2):
    if straw[i] < straw[i+1] + straw[i+2]:
        res = straw[i] + straw[i+1] + straw[i+2]
        break
    else:
        res=-1

print(res)