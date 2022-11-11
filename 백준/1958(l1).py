# 문자열과 놀기를 세상에서 제일 좋아하는 영식이는 오늘도 문자열 2개의 LCS(Longest Common Subsequence)를 구하고 있었다. 어느 날 영식이는 조교들이 문자열 3개의 LCS를 구하는 것을 보았다. 영식이도 도전해 보았지만 실패하고 말았다.
# 이제 우리가 할 일은 다음과 같다. 영식이를 도와서 문자열 3개의 LCS를 구하는 프로그램을 작성하라.

import sys
input = sys.stdin.readline

seq_1 = input().rstrip()
seq_2 = input().rstrip()
seq_3 = input().rstrip()

x = len(seq_1)
y = len(seq_2)
z = len(seq_3)

arr = [[[0] * (z+1) for _ in range(y+1)] for _ in range(x+1)]


for i in range(1, x+1):
    for j in range(1, y+1):
        for k in range(1, z+1):
            if seq_1[i-1] == seq_2[j-1] and seq_2[j-1] == seq_3[k-1]:
                arr[i][j][k] = arr[i-1][j-1][k-1] + 1
            else:
                arr[i][j][k] = max(arr[i][j][k-1], arr[i][j-1][k], arr[i-1][j][k])

ans = -1

for i in range(x+1):
    for j in range(y+1):
        ans = max(max(arr[i][j]), ans)

print(ans)