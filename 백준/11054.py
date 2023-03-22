# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.
# 예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만,  {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.
# 수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [[0, 0] for _ in range(n)] 

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j] and dp[i][0] < dp[j][0]:
            dp[i][0] = dp[j][0]
    dp[i][0] += 1
for i in range(n-1, -1, -1):
    for j in range(n-1, i,-1):
        if arr[i] > arr[j] and dp[i][1] < dp[j][1]:
            dp[i][1] = dp[j][1]
    dp[i][1] += 1
ans = -1
for a, b in dp:
    if ans < (a+b-1):
        ans = (a+b-1)
print(ans)