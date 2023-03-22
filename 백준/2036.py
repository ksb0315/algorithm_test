# n개의 정수로 이루어진 수열이 있다. 이 수열에서 한 정수를 제거하거나, 또는 두 정수를 제거할 수 있다. 한 정수를 제거하는 경우에는 그 정수가 점수가 되고, 두 정수를 제거하는 경우에는 두 정수의 곱이 점수가 된다. 이를 반복하여 수열에 아무 수도 남지 않게 되었을 때, 점수의 총 합의 최대를 구하는 프로그램을 작성하시오.
# 예를 들어 -1, 5, -3, 5, 1과 같은 수열이 있다고 하자. 먼저 1을 제거하고, 다음으로는 5와 5를 제거하고, 다음에는 -1과 -3을 제거했다고 하자. 이 경우 각각 점수가 1, 25, 3이 되어 총 합이 29가 된다.

import sys

input = sys.stdin.readline

n = int(input())

posi=[]
nega=[]
one=[]

for _ in range(n):
    num = int(input())
    if num > 1:
        posi.append(num)
    elif num <= 0:
        nega.append(num)
    else:
        one.append(num)

posi.sort(reverse=True)
nega.sort()
ans = 0

if len(posi) % 2 == 0:
    for i in range(0,len(posi),2):
        ans += posi[i] * posi[i+1]
else:
    for i in range(0,len(posi)-1,2):
        ans += posi[i] * posi[i+1]
    ans += posi[len(posi)-1]

if len(nega) % 2 == 0:
    for i in range(0,len(nega),2):
        ans += nega[i] * nega[i+1]
else:
    for i in range(0,len(nega)-1,2):
        ans += nega[i] * nega[i+1]
    ans += nega[len(nega)-1]

ans += sum(one)

print(ans)