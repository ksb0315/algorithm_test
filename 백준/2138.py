# N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 
# 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 
# 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.
# N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

# import sys
# import copy

# input = sys.stdin.readline

# def switch(ind):
#     if ind == 0:
#         btn[ind] = 1 - btn[ind]
#         btn[ind+1] = 1 - btn[ind+1]
#     elif ind == len(btn) - 1:
#         btn[ind] = 1 - btn[ind]
#         btn[ind-1] = 1 - btn[ind-1]
#     else:
#         btn[ind] = 1 - btn[ind]
#         btn[ind-1] = 1 - btn[ind-1]
#         btn[ind+1] = 1 - btn[ind+1]

# n = int(input())
# lights = list(map(int, input().rstrip()))
# wanted = list(map(int, input().rstrip()))
# changed1 = copy.deepcopy(lights)
# changed2 = copy.deepcopy(lights)
# flag = True

# for _ in range(2):
#     cnt = 0
#     if flag:
#         btn = changed1
#     else: 
#         btn = changed2
#     for i in range(n):
#         if flag:
#             if btn != wanted and i == 0:
#                 switch(i)
#                 cnt += 1
#                 flag = False
#         else:
#             switch(i)
#             cnt += 1
#     if btn == wanted:
#         print(cnt)
#         break
        
# if btn != wanted:
#     print(-1)

import sys

input = sys.stdin.readline

n = int(input())
bulb = list(map(int, input().rstrip()))
target = list(map(int, input().rstrip()))

def change(a, b):
    light = a[:]
    press = 0
    for i in range(1, n):
        if light[i-1] == b[i-1]:
            continue
        press += 1
        for j in range(i-1, i+2):
            if j<n:
                light[j] = 1 - light[j]
    return press if light == b else 1e9

res = change(bulb, target)
bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]
res = min(res, change(bulb, target) + 1)
print(res if res != 1e9 else -1)
