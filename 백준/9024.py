# 여러 개의 서로 다른 정수 S = {a1, a2, …, an} 와 또 다른 정수 K 가 주어졌을 때, S 에 속하는 서로 다른 두 개의 정수의 합이 K 에 가장 가까운 두 정수를 구하시오. 예를 들어, 10 개의 정수
# S = { -7, 9, 2, -4, 12, 1, 5, -3, -2, 0}
# 가 주어졌을 때, K = 8 에 그 합이 가장 가까운 두 정수는 {12, -4} 이다. 또한 K = 4 에 그 합이 가장 가까운 두 정수는 {-7, 12}, {9, -4}, {5, -2}, {5, 0}, {1, 2} 등의 다섯 종류가 있다.
# 여러 개의 서로 다른 정수가 주어졌을 때, 주어진 정수들 중에서 서로 다른 두 정수의 합이 주어진 또 다른 정수에 가장 가까운 두 정수의 조합의 수를 계산하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

case = int(input())

for _ in range(case):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    start = 0
    end = n-1
    check = float('inf')
    cnt = 0

    while start < end:
        if arr[start] + arr[end] > k:
            if abs((arr[start] + arr[end]) - k) < check:
                check = abs(arr[start] + arr[end] - k)
                cnt = 1
            elif abs((arr[start] + arr[end]) - k) == check:
                cnt += 1
            end -= 1
        else:
            if abs((arr[start] + arr[end]) - k) < check:
                check = abs(arr[start] + arr[end] - k)
                cnt = 1
            elif abs((arr[start] + arr[end]) - k) == check:
                cnt += 1
            start += 1
    print(cnt)