# 트리에서 리프 노드란, 자식의 개수가 0인 노드를 말한다.
# 트리가 주어졌을 때, 노드 하나를 지울 것이다. 그 때, 남은 트리에서 리프 노드의 개수를 구하는 프로그램을 작성하시오. 노드를 지우면 그 노드와 노드의 모든 자손이 트리에서 제거된다.
# 예를 들어, 다음과 같은 트리가 있다고 하자.
# 현재 리프 노드의 개수는 3개이다. (초록색 색칠된 노드) 이때, 1번을 지우면, 다음과 같이 변한다. 검정색으로 색칠된 노드가 트리에서 제거된 노드이다.
# 이제 리프 노드의 개수는 1개이다.

import sys

input = sys.stdin.readline

def delNode(d):
    global cnt
    if tree[d]:
        if len(tree[d]) == 2:
            if tree[d][0]:
                delNode(tree[d][0])
            if tree[d][1]:
                delNode(tree[d][1])
            if not tree[d][0]:
                cnt += 1
        else:
            if tree[d][0]:
                delNode(tree[d][0])
            if not tree[d][0]:
                cnt += 1
    else:
        cnt += 1

n = int(input())
nodes = list(map(int, input().split()))
d = int(input())
tree = [[] for _ in range(n)]

for i in range(n):
    if nodes[i] == -1:
        continue
    tree[nodes[i]].append(i)

cnt_leaf = 0
for i in range(len(tree)):
    if not tree[i]:
        cnt_leaf += 1

cnt = 0
delNode(d)

if cnt_leaf - cnt == 0 and n > 1:
    print(1)
elif cnt_leaf - cnt == 0 and n == 1:
    print(0)
else:
    print(cnt_leaf - cnt)