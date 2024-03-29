# 다음과 같이 정의된 수열이 있다.
# D[1] = A
# D[n] = D[n-1]의 각 자리의 숫자를 P번 곱한 수들의 합
# 예를 들어 A=57, P=2일 때, 수열 D는 [57, 74(=52+72=25+49), 65, 61, 37, 58, 89, 145, 42, 20, 4, 16, 37, …]이 된다. 그 뒤에는 앞서 나온 수들(57부터가 아니라 58부터)이 반복된다.
# 이와 같은 수열을 계속 구하다 보면 언젠가 이와 같은 반복수열이 된다. 이때, 반복되는 부분을 제외했을 때, 수열에 남게 되는 수들의 개수를 구하는 프로그램을 작성하시오. 위의 예에서는 [57, 74, 65, 61]의 네 개의 수가 남게 된다.

import sys

input = sys.stdin.readline

a, p = map(int, input().split())
arr = [a]

while True:
    temp = 0
    for s in str(arr[-1]):
        temp += int(s) ** p
    
    if temp in arr:
        break

    arr.append(temp)

print(len(arr[:arr.index(temp)]))    
    