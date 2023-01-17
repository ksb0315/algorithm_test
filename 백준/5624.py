# 정수 N개로 이루어진 수열 A가 있다. 이때, i번째 수가 그 앞에 있는 수 세 개의 합으로 나타낼 수 있을 때, 그 수를 좋다고 한다. (같은 위치에 있는 수를 여러 번 더해도 된다)
# 수열이 주어졌을 때, 총 몇 개의 수가 좋은 수 일까?

import sys
input = sys.stdin.readline

n = int(input())
s = set()

arr = list(map(int, input().split()))

result = 0
s.add(arr[0] + arr[0])

for i in range(1, n):
    for j in range(i):
        if arr[i] - arr[j] in s:
            result += 1
            break
    
    for j in range(i+1):
        s.add(arr[i] + arr[j])

print(result)