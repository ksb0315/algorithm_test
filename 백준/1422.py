# 숫자의 신은 여러명이 있지만, 그 중에 자연수의 신은 오세준이다. 오세준은 자연수의 신으로 오래오래 살다가 어느 날 음수의 신과 전쟁을 하게 되었다. 오세준은 음수의 신 이다솜을 이기기위해서 큰 숫자를 만들기로 했다.
# 오세준은 지금 K개의 자연수를 가지고 있다. 오세준은 K개의 수 중에 정확하게 N개의 수를 뽑아내서 그 수를 붙여서 만들 수 있는 수중에 가장 큰 수를 만들고자 한다. 같은 수를 여러 번 이용해도 된다. 단, 모든 수는 적어도 한 번은 이용되어야 한다.
# 오세준이 현재 가지고 있는 K개의 수가 주어졌을 때, 이 수를 적어도 한 번 이상 이용해서 만들 수 있는 수 중에 가장 큰 수를 출력하는 프로그램을 작성하시오.
# 예를 들어 지금 오세준이 2, 3, 7 이라는 3개의 수를 가지고 있고, 4개의 수를 뽑아야 한다면, 7732를 만들면 가장 큰 수가 된다.

import heapq
from functools import cmp_to_key

def compare(a, b):
    return int(str(a)+str(b)) - int(str(b)+str(a))

k, n = map(int, input().split())
nums = [int(input()) for _ in range(k)]

max_num = max(nums)
for _ in range(n - len(nums)):
    nums.append(max_num)
nums= sorted(nums, key=cmp_to_key(lambda a, b: -1 if int(str(a)+str(b)) > int(str(b)+str(a)) else 1))
print(*nums, sep='')
