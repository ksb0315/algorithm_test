# P[0], P[1], ...., P[N-1]은 0부터 N-1까지(포함)의 수를 한 번씩 포함하고 있는 수열이다. 수열 P를 길이가 N인 배열 A에 적용하면 길이가 N인 배열 B가 된다. 적용하는 방법은 B[P[i]] = A[i]이다.
# 배열 A가 주어졌을 때, 수열 P를 적용한 결과가 비내림차순이 되는 수열을 찾는 프로그램을 작성하시오. 비내림차순이란, 각각의 원소가 바로 앞에 있는 원소보다 크거나 같을 경우를 말한다. 만약 그러한 수열이 여러개라면 사전순으로 앞서는 것을 출력한다.

import sys

input = sys.stdin.readline

n = int(input())

a_arr = list(map(int,input().split()))

b_arr = []
for i in range(n):
    b_arr.append([a_arr[i], i, 0])

b_arr.sort(key=lambda x : x[0])

for i in range(n):
    b_arr[i][2] = i

b_arr.sort(key=lambda x : x[1])

for i in range(n):
    print(b_arr[i][2], end=' ')