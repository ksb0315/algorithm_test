# n과 l이 주어질 때, 합이 n이면서, 길이가 적어도 l인 가장 짧은 연속된 음이 아닌 정수 리스트를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n, l = map(int, input().split())

for i in range(l, 101):
    x = n - (i * (i + 1) / 2)

    if x % i == 0:
        x = int(x / i)

        if x >= -1:
            for j in range(1, i + 1):
                print(x + j, end=' ')
            print()
            break
else:
    print(-1)