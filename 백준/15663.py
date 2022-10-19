# N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.
# N개의 자연수 중에서 M개를 고른 수열

import sys
# import copy

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int,input().split())))

s = []
temp = []
ans = []
count = {}
 
def dfs():
    if len(s)==m:
        # temp.append(copy.deepcopy(tuple(s)))
        print(' '.join(map(str,s)))
        return
    
    for i in range(n):
        s.append(nums[i])
        dfs()
        s.pop()


for i in range(len(nums)):
    count[nums[i]] = nums.count(nums[i])

dfs()
# temp = sorted(list(set(temp)))

# for group in temp:
#     flag = False
#     for i in range(len(group)):
#         if len(group) == 1:
#             flag = True
#         else:
#             if group.count(group[i]) == count[group[i]]:
#                 flag = True
#     if flag:
#         ans.append(list(group))

# for a in ans:
#     print(*a)