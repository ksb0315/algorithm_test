# 수열 A가 주어졌을 때, 그 수열의 증가 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
# 예를 들어, 수열 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 인 경우에 합이 가장 큰 증가 부분 수열은 A = {1, 100, 2, 50, 60, 3, 5, 6, 7, 8} 이고, 합은 113이다.

import sys

input = sys.stdin.readline

n=int(input())
array=list(map(int, input().split()))

dp=[0]*n
dp[0]=array[0]
for i in range(1,n):
  for j in range(i):
    if array[j]<array[i]:
      dp[i]=max(dp[i], dp[j]+array[i])
    else:
      dp[i]=max(dp[i], array[i])

print(max(dp))