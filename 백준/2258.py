# 은혜는 정육점에서 고기를 사려고 한다. 보통 정육점에서는 자신이 원하는 양을 이야기하면 그 양만큼의 고기를 팔지만, 은혜가 방문한 정육점에서는 세일 행사를 하고 있었기 때문에 N 덩어리의 고기를 이미 잘라놓고 판매하고 있었다.
# 각각의 덩어리들은 이미 정해져 있는 무게와 가격이 있는데, 어떤 덩어리를 샀을 때에는 그 덩어리보다 싼 고기들은 얼마든지 덤으로 얻을 수 있다(추가 비용의 지불 없이).
# 또한 각각의 고기들은 부위가 다를 수 있기 때문에 비용과 무게와의 관계가 서로 비례하는 관계가 아닐 수도 있다. 은혜는 이러한 점을 고려하지 않고, 어느 부위든지 자신이 원하는 양만 구매하면 되는 것으로 가정한다. 또한 만약 가격이 더 싸다면 은혜가 필요한 양보다 더 많은 고기를 살 수도 있다.
# 각 덩어리에 대한 정보가 주어졌을 때, 은혜가 원하는 양의 고기를 구매하기 위해 필요한 최소 비용을 계산하는 프로그램을 작성하시오.

import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((b, a))
arr = sorted(arr, key=lambda x: (x[0], -x[1]))

ans = sys.maxsize
weight, same = 0, 0
flag = False

for i in range(n):
    weight += arr[i][1]
    if i >= 1 and arr[i][0] == arr[i - 1][0]:
        same += arr[i][0]
    else:
        same = 0
    if weight >= m:
        ans = min(ans, arr[i][0] + same)
        flag = True
        
print(ans if flag else -1)