# RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.
# 집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.
# 1번 집의 색은 2번, N번 집의 색과 같지 않아야 한다.
# N번 집의 색은 N-1번, 1번 집의 색과 같지 않아야 한다.
# i(2 ≤ i ≤ N-1)번 집의 색은 i-1, i+1번 집의 색과 같지 않아야 한다.

import sys

input = sys.stdin.readline
INF = float('inf')


n = int(input())
rgb = []
ans = INF
for _ in range(n):
    rgb.append(list(map(int, input().split())))

for i in range(3):
    dp = [[INF, INF, INF] for _ in range(n)]
    dp[0][i] = rgb[0][i]
    for j in range(1, n):
        dp[j][0] = rgb[j][0] + min(dp[j-1][1], dp[j-1][2])
        dp[j][1] = rgb[j][1] + min(dp[j-1][0], dp[j-1][2])
        dp[j][2] = rgb[j][2] + min(dp[j-1][0], dp[j-1][1])

    for j in range(3):
        if i != j:
            ans = min(ans, dp[-1][j])
print(ans)
