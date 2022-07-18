# 양의 정수 b와 n이 주어졌을 때, b에 가장 가까운 An의 정수 A를 찾는 프로그램을 작성하시오. An은 b보다 작거나, 크거나, 같다.

import sys

input = sys.stdin.readline

while True:
    b, n = map(int, input().split())
    if b == n == 0:
        break
    i = 0
    while i**n < b:
        i += 1
    print(i if i**n-b < b-(i-1)**n else i-1)



