# 자연수 X를 소인수분해하면, 곱해서 X가 되는 소수의 목록을 얻을 수 있다. 예를 들어, 12 = 2 × 2 × 3이다. 1은 소수가 아니다.
# 어떤 수 X를 소인수분해 해서 구한 소수의 목록의 길이가 소수이면, 그 수를 언더프라임 이라고 한다. 12는 목록에 포함된 소수의 개수가 3개이고, 3은 소수이니 12는 언더프라임이다.
# 두 정수 A와 B가 주어졌을 때, A보다 크거나 같고, B보다 작거나 같은 정수 중에서 언더프라임인 것의 개수를 구해보자.

import sys

input = sys.stdin.readline

a,b = map(int,input().split())
prime = [True for _ in range(100001)]
prime[1] = False

m = int(100000 ** 0.5)
for n in range(2,m+1) :
    if prime[n] :
        for k in range(n,100001) :
            if n * k > 100000 :
                break
            prime[n*k] = False
    if n * (n+1) > 100000 :
        break

prime_len = [0 for _ in range(b+1)]

for i in range(1,b+1) :
    if prime[i] :
        prime_len[i] = 1
for i in range(2,b+1) :
    for j in range(2,b+1) :
        if i * j > b :
            break
        if prime[j] :
            prime_len[i*j] = prime_len[i] + 1


ans = 0
for i in range(a,b+1) :
    if prime[prime_len[i]] :
        ans +=1

print(ans)