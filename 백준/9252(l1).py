# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

import sys

input = sys.stdin.readline

str1 = [""] + list(input().rstrip())
str2 = [""] + list(input().rstrip())
path = [[""]*len(str2) for _ in range(len(str1))]

for i in range(1, len(str1)):
    for j in range(1, len(str2)):
        if str1[i] == str2[j]:
            path[i][j] = path[i-1][j-1] + str1[i]
        else:
            if len(path[i-1][j]) >= len(path[i][j-1]):
                path[i][j] = path[i-1][j]
            else:
                path[i][j] = path[i][j-1]

ans = path[-1][-1]
print(len(ans))
print(ans)