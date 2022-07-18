# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

import sys

input = sys.stdin.readline

m = int(input())
n = int(input())

ans = []
def prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

for i in range(m, n + 1):
    if i==1:
        pass
    elif i==2:
        ans.append(i)
    elif prime(i):
        ans.append(i)

if len(ans) > 0:
    print(sum(ans))
    print(min(ans))
else:
    print(-1)