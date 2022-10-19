# 정연이는 트럼프 카드 (Playing Card)로 할 수 있는 새로운 게임을 만들기로 결심했다.
# 우선 이 게임은 딜러와 플레이어가 1:1로 플레이한다. 그리고 플레이어는 놓여진 52장의 트럼프 카드에서 N장의 카드를 뽑는다. 뽑은 카드들로 "포카드 (four of a kind)" 족보를 만들 수 있다면 플레이어의 승리, 만들 수 없다면 딜러의 승리로 게임이 끝난다. 그러나 정연이는 아직 공정한 게임을 위한, 뽑는 카드의 수 N을 결정하지 못하였다.
# 정연이가 쉽게 결정을 내릴 수 있도록, N개의 카드를 뽑았을 때 플레이어가 이기는 경우의 수를 출력하는 프로그램을 작성해주자.
# 트럼프 카드는 다음과 같은 52장의 카드로 구성된다.
# Figure: 트럼프 카드 (Playing Card)의 구성
# 문양 4개: ♥, ♠, ◆, ♣, 숫자 13개: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K
# 총 4 x 13 = 52장
# 포카드 (four of a kind)는 뽑은 N장의 카드 중에 "같은 숫자를 가진, 다른 문양의 4장의 카드"가 존재하는 경우를 의미한다. 또한 플레이어가 이기는 경우의 수는 N장의 카드에 이러한 카드 조합을 1쌍 이상 포함하고 있는 경우의 수를 의미한다.

import sys, math
input = sys.stdin.readline

def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

n = int(input())

dp = [[0] * 14 for _ in range(n + 1)]
mod = 10007

dp[0][0] = 1
for i in range(n):
    for j in range(13):
        for k in range(4):
            if i + k <= n:
                dp[i + k][j + 1] += dp[i][j] * combination(4, k)
idx = 1
ans = 0
while 4 * idx <= n:
    temp = combination(13, idx)
    ans += temp * dp[n - 4 * idx][13 - idx]
    ans %= mod
    idx += 1
    
print(ans % mod)