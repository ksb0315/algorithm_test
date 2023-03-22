# n개의 서로 다른 양의 정수 a1, a2, ..., an으로 이루어진 수열이 있다. ai의 값은 1보다 크거나 같고, 1000000보다 작거나 같은
# 자연수이다. 자연수 x가 주어졌을 때, ai + aj = x (1 ≤ i < j ≤ n)을 만족하는 (ai, aj)쌍의 수를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int, input().split())))
x = int(input())

cnt = 0
start = 0
end = n-1

while start < end:
        temp = arr[start] + arr[end]
        if temp == x: cnt += 1
        if temp < x:
            start += 1
            continue
        end -= 1

print(cnt)
