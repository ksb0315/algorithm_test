# 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
n = int(input())
sum = 0
res = 0

while True:
    res = res+1
    sum += res
    if sum > n:
        res -= 1
        break
    elif sum == n:
        break
print(res)
