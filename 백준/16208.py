# 현우는 무슨 이유에선지 길이 a1, ..., an의, 총 n개의 쇠막대가 필요해졌다. 하지만 그가 가진 것은 길이 a1+...+an의 하나의 쇠막대뿐이었다. 
# 현우는 이 막대를 직접 잘라서 원래 필요하던 n개의 쇠막대를 만들 것이다. 길이 x+y인 막대를 길이 x, y인 두 개의 막대로 자를 때에는 만들려 하는 두 막대의 길이의 곱인 xy의 비용이 든다. 현우는 최소의 비용으로 이 쇠막대를 잘라서 a1, ..., an의 n개의 쇠막대를 얻고 싶다.
# 그런데 현우는 이 비용이 얼마나 들지 잘 모르겠다. 그래서 여러분이 막대를 자르는 최소 비용을 계산하는 프로그램을 작성해주면 코드잼 경시대회 점수를 30점 올려주겠다고 제안했다. 어떤가?

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
total = sum(arr)
answer  = 0
for num in arr:
    answer += num * (total - num)
    total -= num
print(answer)