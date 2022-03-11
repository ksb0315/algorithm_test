# 구사과국은 동전만 사용하고, 동전의 가치는 다음과 같다.
# 1, 10, 25, 100, 1000, 2500, 10000, 100000, 250000, 1000000 ...
# 즉, 식으로 표현하면 K ≥ 0를 만족하는 모든 K에 대해서, 가치가 10K인 동전과 25×100K인 동전이 있는 것이다.
# 구사과국에 살고 있는 구사과는 초콜릿을 하나 구매해 5차원 세계로 이사가려고 한다. 초콜릿의 가격이 주어졌을때, 이를 구매하기 위해 필요한 동전 개수의 최솟값을 구해보자. 각 동전의 개수는 무한하고, 구매할 때는 정확하게 초콜릿의 가격만큼만 지불해야 한다.
coin = [1, 10, 25]
dp = [0] * 100
for i in range(1, len(dp)):
    dp[i] = float('inf')
    for j in range(len(coin)):
        if (i - coin[j]) >= 0:
            dp[i] = min(dp[i], dp[i-coin[j]] + 1)
t = int(input())
ans = []
for i in range(t):
    n = int(input())
    coin_count = 0
    while n > 0:
        lt_100 = n % 100
        coin_count += dp[lt_100]
        n = int(n/100)
    ans.append(coin_count)
for i in ans:
    print(i)