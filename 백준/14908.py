# 지금 구두 수선공에게는 손님으로부터 주문 받고 제작해야 할 작업이 N개 쌓여있다. 구두 수선공은 하루에 한 작업만 수행할 수 있고, i번째 작업을 완료하는 데 Ti일이 걸린다. 이때 Ti는 정수이고 1 ≤ Ti ≤ 1000이다.
# i번째 작업을 시작하기 전에 하루가 지연될 때마다 구두 수선공은 보상금 Si센트를 지불해야 한다. 이때 Si는 정수이고 1 ≤ Si ≤ 10000이다. 구두 수선공을 돕기 위해 최저 보상금을 지불하는 작업 순서를 정해야 한다.
# 하루에 2개 이상의 작업을 동시에 수행할 수 없다. 작업 i를 수행하고 있는 경우, 작업 i를 마칠 때 까지 작업 i 외의 다른 작업을 수행할 수 없다.

import sys

input = sys.stdin.readline

n = int(input())
works_ratio = []
for i in range(1, n+1):
    t,s = map(int,input().split())
    works_ratio.append((t/s, i))

works_ratio.sort()

for w, num in works_ratio:
    print(num)