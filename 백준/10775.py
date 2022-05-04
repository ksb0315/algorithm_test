# 오늘은 신승원의 생일이다.
# 박승원은 생일을 맞아 신승원에게 인천국제공항을 선물로 줬다.
# 공항에는 G개의 게이트가 있으며 각각은 1에서 G까지의 번호를 가지고 있다.
# 공항에는 P개의 비행기가 순서대로 도착할 예정이며, 당신은 i번째 비행기를 1번부터 gi (1 ≤ gi ≤ G) 번째 게이트중 하나에 영구적으로 도킹하려 한다. 비행기가 어느 게이트에도 도킹할 수 없다면 공항이 폐쇄되고, 이후 어떤 비행기도 도착할 수 없다.
# 신승원은 가장 많은 비행기를 공항에 도킹시켜서 박승원을 행복하게 하고 싶어한다. 승원이는 비행기를 최대 몇 대 도킹시킬 수 있는가?

import sys

def find_parent(x):
    if parent[x] == x:
        return x
    P = find_parent(parent[x])
    parent[x] = P
    return parent[x]

def union(x, y):
    x = find_parent(x)
    y = find_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

read = sys.stdin.readline
G = int(read().strip("\n"))
P = int(read().strip("\n"))

# union - find의 핵심
# {0:0, 1:1, 2:2, 3:3, 4:4}
parent = {i: i for i in range(0, G+1)}
planes = []
count = 0

for _ in range(P):
    planes.append(int(read().strip("\n")))

for plane in planes:
    x = find_parent(plane)

    if x == 0:
        break
    union(x, x-1)
    count += 1

print(count)