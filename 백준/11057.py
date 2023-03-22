# 오르막 수는 수의 자리가 오름차순을 이루는 수를 말한다. 이때, 인접한 수가 같아도 오름차순으로 친다.
# 예를 들어, 2234와 3678, 11119는 오르막 수이지만, 2232, 3676, 91111은 오르막 수가 아니다.
# 수의 길이 N이 주어졌을 때, 오르막 수의 개수를 구하는 프로그램을 작성하시오. 수는 0으로 시작할 수 있다.

import sys

input = sys.stdin.readline

n = int(input())
dp = [[1] * 10]

for i in range(1, n+1):
    dp.append([1])
    for j in range(1, 10):
        dp[i].append(dp[i][j-1] + dp[i-1][j])

ans = dp[-1][-1] % 10007
print(ans)
