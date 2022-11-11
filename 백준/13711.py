# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, [1, 2, 3]과 [1, 3, 2]의 LCS는 [1, 2] 또는 [1, 3] 이다. 
# 1부터 N까지 정수가 모두 한 번씩 등장하는 두 수열 A와 B가 주어졌을 때, 두 수열의 LCS 크기를 구하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n = int(input())

seq1 = list(map(int, input().split()))
seq2 = list(map(int, input().split()))

x = len(seq1)
y = len(seq2)

dp = [[0] * (y+1) for _ in range(x+1)]

for i in range(1, x+1):
    for j in range(1, y+1):
        if seq1[i-1] == seq2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])