# 박성원은 이 문제를 풀지 못했다.
# 서로 다른 정수로 이루어진 집합이 있다. 이 집합의 순열을 합치면 큰 정수 하나를 만들 수 있다. 예를 들어, {5221,40,1,58,9}로 5221401589를 만들 수 있다. 합친수가 정수 K로 나누어 떨어지는 순열을 구하는 프로그램을 작성하시오.
# 하지만, 박성원은 이 문제를 풀지 못했다.
# 따라서 박성원은 그냥 랜덤하게 순열 하나를 정답이라고 출력하려고 한다. 이 문제에는 정답이 여러 개 있을 수도 있고, 박성원이 우연히 문제의 정답을 맞출 수도 있다.
# 박성원이 우연히 정답을 맞출 확률을 분수로 출력하는 프로그램을 작성하시오.

from itertools import permutations
import fractions
import sys, math

input = sys.stdin.readline

def solution(mod,bit):
    if bit == (1 << n) - 1:
        if mod == 0:
            return 1
        return 0
    if dp[mod][bit] != -1:
        return dp[mod][bit]
    temp = 0
    for j in range(n):
        if not bit & (1 << j):
            new_mod = ((mod * mod_10[arr_length[j]]) % k + arr[j]) % k
            temp += solution(new_mod, bit | 1 << j)
    dp[mod][bit] = temp
    return dp[mod][bit]

n = int(input())
arr = [int(input()) for _ in range(n)]
k = int(input())
arr_length = [len(str(i)) for i in arr]
arr = [i % k for i in arr]

mod_10 = [1]
for i in range(50):
    mod_10.append((mod_10[-1]*10) % k)

dp = [[-1]*(1 << n) for _ in range(k)]
ans = solution(0,0)

if ans == 0:
    print('0/1')
else:
    fact = math.factorial(n)
    if ans == fact or k == 1:
        print('1/1')
    elif ans == 0:
        print('0/1')
    else:
        print(fractions.Fraction(ans, fact))