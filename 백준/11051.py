# 자연수 \(N\)과 정수 \(K\)가 주어졌을 때 이항 계수 \(\binom{N}{K}\)를 10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

pascal = [0]
for depth in range(2, n+2):
    pascal.append([0]*depth)

pascal[1] = [1, 1]

for depth in range(2, n):
    pascal[depth][0] = 1
    for idx in range(1, depth):
        pascal[depth][idx] = (pascal[depth-1][idx-1] + pascal[depth-1][idx]) % 10007
    pascal[depth][-1] = 1

if k == 0 or k == n:
    print(1)
else:
    print((pascal[n-1][k-1] + pascal[n-1][k]) % 10007)