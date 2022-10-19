# n개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 “좋다(GOOD)”고 한다.
# n개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라.
# 수의 위치가 다르면 값이 같아도 다른 수이다.

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr = sorted(arr)
ans = 0

for i in range(n):
    temp = arr[:i] + arr[i + 1:]
    left, right = 0, len(temp) - 1
    while left < right:
        t = temp[left] + temp[right]
        if t == arr[i]:
            ans += 1    
            break
        elif t < arr[i]: 
            left += 1
        else: 
            right -= 1
print(ans)
