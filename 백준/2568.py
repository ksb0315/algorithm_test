# 두 전봇대 A와 B 사이에 하나 둘씩 전깃줄을 추가하다 보니 전깃줄이 서로 교차하는 경우가 발생하였다. 합선의 위험이 있어 이들 중 몇 개의 전깃줄을 없애 전깃줄이 교차하지 않도록 만들려고 한다.
# 예를 들어, <그림 1>과 같이 전깃줄이 연결되어 있는 경우 A의 1번 위치와 B의 8번 위치를 잇는 전깃줄, A의 3번 위치와 B의 9번 위치를 잇는 전깃줄, A의 4번 위치와 B의 1번 위치를 잇는 전깃줄을 없애면 남아있는 모든 전깃줄이 서로 교차하지 않게 된다. 
# 전깃줄이 전봇대에 연결되는 위치는 전봇대 위에서부터 차례대로 번호가 매겨진다. 전깃줄의 개수와 전깃줄들이 두 전봇대에 연결되는 위치의 번호가 주어질 때, 남아있는 모든 전깃줄이 서로 교차하지 않게 하기 위해 없애야 하는 최소 개수의 전깃줄을 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

def lower_bound(left, right, a, x):
    while left <= right:
        mid = (left + right) // 2
        if a[mid] >= x:
            right = mid - 1
        else:
            left = mid + 1
    return left

n = int(input())

a = []
for i in range(n):
    start, end = map(int, input().split())
    a.append((start, end))
    
a.sort(key=lambda x : x[0])
d = [a[0][1]]
q = [-1] * n

for i in range(n):
    if d[-1] < a[i][1]:
        q[i] = max(q) + 1
        d.append(a[i][1])
    else:
        x = lower_bound(0,len(d) - 1, d, a[i][1])
        if a[i][1] > d[x]:
            d[-1] = a[i][1]
        else:
            d[x] = a[i][1]
            q[i] = x + 1

print(n - len(d))
r = len(d)
w = []

for i in range(n - 1, -1, -1):
    if r == 0:
        break
    if q[i] == r:
        w.append(a[i])
        r -= 1
        
c = []
for i in a:
    if i not in w:
        c.append(i)
      
c.sort(key=lambda x : x[0])
for i in range(n - len(d)):
    print(c[i][0])
