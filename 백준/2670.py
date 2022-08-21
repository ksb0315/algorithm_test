# N개의 실수가 있을 때, 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아, 그 곱을 출력하는 프로그램을 작성하시오. 예를 들어 아래와 같이 8개의 양의 실수가 주어진다면,

# 색칠된 부분의 곱이 최대가 되며, 그 값은 1.638이다.

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(float(input().rstrip()))

ans = arr[0]
for i in range(n):
    temp = arr[i]
    if ans < arr[i]:
        ans = arr[i]
    for j in range(i+1, n):        
        if ans < arr[j] * temp:
            ans = arr[j] * temp
        temp = arr[j] * temp

print("%.3f" %(ans))