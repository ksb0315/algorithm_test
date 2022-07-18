# n개의 정수 A[1], A[2], …, A[n]이 있다. 서로 다른 세 정수 i, j, k에 대해서 a = A[i], b = A[j], c = A[k]라 하자. 세 수의 중위(Median)값은 정렬했을 때 가운데에 오는 수가 된다. 세 수의 평균(Mean)값은 (a+b+c)÷3이 된다.
# 만약 세 수가 5, 2, 5라면 중위값은 5, 평균값은 4가 된다. 세 수가 2, 3, 1이라면 중위값은 2, 평균값도 2가 된다.
# n개의 수들이 주어졌을 때, 위와 같이 세 수를 선택하여(i, j, k가 서로 다르도록) 중위값과 평균값의 차이가 최대가 되도록 해 보시오.

import sys 

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

ans = 0
for i in range(1, n-1):
    mid = arr[i] * 3

    mean1 = arr[i-1] + arr[i] + arr[-1]
    mean2 = arr[0] + arr[i] + arr[i+1]

    temp = max(abs(mean1-mid), abs(mean2-mid))
    ans = max(ans, temp)
print(ans)