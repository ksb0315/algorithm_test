# 여자친구가 없는 남자 n명과 남자친구가 없는 여자 m명을 불러 모아서 이성 친구를 만들어 주기로 하였다. 하지만 아무렇게나 해줄 수는 없고, 최대한 비슷한 성격의 사람들을 짝 지어 주기로 하였다.
# 당신은 뭔가 알 수 없는 방법으로 각 사람의 성격을 수치화 하는데 성공하였다. 따라서 각 사람의 성격은 어떤 정수로 표현된다. 
# 이와 같은 성격의 수치가 주어졌을 때, 우선 최대한 많은 커플을 만들고, 각 커플을 이루는 두 사람의 성격의 차이의 합이 최소가 되도록 하려 한다. 남자-여자 커플만 허용된다.
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
boys = list(map(int, input().split()))
girls = list(map(int, input().split()))
if n > m: 
    boys, girls = girls, boys
    n, m = m, n
dp = [[0] * m for __ in range(n)]
boys.sort(); girls.sort()

dp[0][0] = abs(boys[0] - girls[0])
for j in range(1, m - (n - 1)):
    dp[0][j] = min(abs(boys[0] - girls[j]), dp[0][j - 1])
    
for i in range(1, n):
    for j in range(i, m - (n - i - 1)):
        if i == j:
            dp[i][j] = dp[i - 1][j - 1] + abs(boys[i] - girls[j])
        else:
            dp[i][j] = min(dp[i - 1][j - 1] + abs(boys[i] - girls[j]), dp[i][j - 1])
print(dp[n - 1][m - 1])