# 1부터 n까지 정수 n개로 이루어진 순열을 나타내는 방법은 여러 가지가 있다. 예를 들어, 8개의 수로 이루어진 순열 (3, 2, 7, 8, 1, 4, 5, 6)을 배열을 이용해 표현하면 <graph>와 같다. 또는, Figure 1과 같이 방향 그래프로 나타낼 수도 있다
# 순열을 배열을 이용해 i에서 πi로 간선을 이어 그래프로 만들 수 있다.
# Figure 1에 나와있는 것 처럼, 순열 그래프 (3, 2, 7, 8, 1, 4, 5, 6) 에는 총 3개의 사이클이 있다. 이러한 사이클을 "순열 사이클" 이라고 한다. n개의 정수로 이루어진 순열이 주어졌을 때, 순열 사이클의 개수를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

def dfs(v):
    visited[v]=1
    next=arr[v]
    if not visited[next]:
        dfs(next)

case = int(input())
ans = []

for _ in range(case):
    cnt = 0
    n = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)

    for i in range(1, n+1):
        if visited[i]==0:
            dfs(i)
            cnt+=1
    ans.append(cnt)

for a in ans:
    print(a)