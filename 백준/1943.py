# 윤화와 준희는 솔선수범하여 쓰레기를 줍는 착한 일을 하였다. 원장선생님께서는 윤화와 준희를 칭찬하시고 과자나 사 먹으라고 하시며 동전 몇 개를 윤화와 준희에게 건네 주었다.
# 그런데 돈을 받은 윤화와 준희는 좋아하기보다 고민에 빠지고 말았다. 원장선생님께 받은 이 돈을 어떻게 나누어 할지 고민에 빠진 것이다. 두 사람 모두 상대방이 자기보다 1원이라도 더 받는 것은 도저히 인정할 수 없어 한다. 따라서 돈을 똑같이 둘로 나누어 가져야 두 사람이 모두 만족할 수 있게 된다.
# 하지만 두 사람에게 돈을 똑같이 나누는 것이 불가능한 경우도 있다. 예를 들어 500원짜리 1개와 50원짜리 1개를 받았다면, 이 돈을 두 사람이 똑같이 나누어 가질 수는 없다. 물론 동전을 반으로 잘라서 나누어 가질 수도 있겠지만 그러면 돈으로서의 가치를 잃기 때문에 그렇게 할 수는 없다.
# 이제 우리가 할 일은 다음과 같다. 원장 선생님께서 N가지 종류의 동전을 각각 몇 개씩 주셨을 때, 그 돈을 반으로 나눌 수 있는지 없는지 판단하는 것이다.

import sys
input = sys.stdin.readline

ans = []

for _ in range(3):
    N = int(input())
    coins = {}
    target = 0

    for _ in range(N):
        a, b = map(int, input().split())
        coins[a] = b
        target += a*b

    if target & 1: # target이 홀수일때 비트연산으로
        ans.append(0)
        continue
    
    target //= 2
    dp = [1] + [0] * (target)
    
    for coin in coins:
        for money in range(target,coin-1,-1):
            if dp[money-coin]:
                for j in range(coins[coin]):
                    if money + coin*j <= target:
                        dp[money + coin*j] = 1
    ans.append(dp[target])

for a in ans:
    print(a)