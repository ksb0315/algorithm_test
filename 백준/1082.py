# 스타트링크가 입주한 사무실은 방 번호를 직접 정할 수 있다. 방 번호를 정하려면 1층 문방구에서 파는 숫자를 구매해야 한다. 숫자를 구매하기 위해 준비한 금액은 M원이고, M원을 모두 사용해야 한다.
# 문방구에서 파는 숫자는 0부터 N-1까지이고, 각 숫자 i의 가격은 Pi이다. 문방구에서는 같은 숫자를 여러 개 구매할 수 있고, 문방구는 매우 많은 재고를 보유하고 있기 때문에, 항상 원하는 만큼 숫자를 구매할 수 있다. 방 번호가 0이 아니라면 0으로 시작할 수 없다.
# 예를 들어, N = 3, M = 21, P0 = 6, P1 = 7, P2 = 8이라면, 만들 수 있는 가장 큰 방 번호는 210이다. M원을 모두 사용해서 만들 수 있는 가장 큰 방 번호를 구해보자.

import sys

N=int(input())
L=list(map(int,input().split()))
money=int(input())

minCost=min(L)
minNum=L.index(minCost)
if N==1:
    print(0)
    sys.exit()

def add(remainMoney,digit):
    for i in range(digit,-1,-1):
        if pick[i]!=N-1:
            for j in range(N-1,pick[i],-1):
                nowCost=L[j]-L[pick[i]]
                if nowCost<=remainMoney:
                    pick[i]=j
                    add(remainMoney-nowCost,digit-1)
                    return
    if not any(pick):
        if not pick:
            print(0)
            sys.exit()
        pick.pop()
        add(remainMoney+L[0],digit-1)

num=money//minCost
pick=[minNum for i in range(num)]
cost=num*minCost
add(money-cost,num-1)
ans=0
for i in range(len(pick)):
    ans+=(10**i)*pick[i]
print(ans)