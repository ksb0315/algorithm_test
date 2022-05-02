# 수 N개 A1, A2, ..., AN이 주어진다. 이때, 연속된 부분 구간의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램을 작성하시오.
# 즉, Ai + ... + Aj (i ≤ j) 의 합이 M으로 나누어 떨어지는 (i, j) 쌍의 개수를 구해야 한다.

import sys
n, m = map(int, input().split())
arr_n = list(map(int, sys.stdin.readline().split()))
arr_m = [0 for _ in range(m)]

s = 0
num = 0
for i in range(n):
    s += arr_n[i]
    res = s % m

    if res == 0:
        num += 1
    
    arr_m[res] += 1


for i in range(m):
    if arr_m == 0:
        continue

    num += arr_m[i] * (arr_m[i] - 1) / 2

print(int(num))