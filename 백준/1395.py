# 준규네 집에는 총 N개의 스위치가 있고 이를 편하게 1번부터 N번까지 차례대로 번호를 매겼다. 그리고 준규의 취미는 이 스위치들을 켜고 끄는 것이다.
# 준규가 하는 스위치를 갖고 노는 일은 크게 두 가지이다. 하나는 A번부터 B번 사이의 스위치 상태를 반전시키는 것이고 다른 하나는 C번부터 D번 사이의 스위치 중 켜져 있는 상태의 스위치의 개수를 세는 것이다.
# 하지만 준규가 싫증을 느껴 우리가 이 귀찮은 일을 떠맡게 되었고 프로그래밍을 통해 일을 처리하도록 결정하였다.

n,m, = map(int,input().split())
bulbs = [False for _ in range(n)]
bulbs.append(False)
ans = []
def reverse(x, y):
    global bulbs
    for i in range(y-x+1):
        if bulbs[x+i]:
            bulbs[x+i] = False
        else:
            bulbs[x+i] = True

for i in range(m):
    o,s,t = map(int, input().split())
    if o == 0:
        reverse(s,t)
    elif o == 1:
        ans.append(bulbs[s:t+1].count(True))

for a in ans:
    print(a)
