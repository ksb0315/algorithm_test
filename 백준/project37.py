# 주사위는 위와 같이 생겼다. 주사위의 여섯 면에는 수가 쓰여 있다. 위의 전개도를 수가 밖으로 나오게 접는다.
# A, B, C, D, E, F에 쓰여 있는 수가 주어진다.
# 지민이는 현재 동일한 주사위를 N3개 가지고 있다. 이 주사위를 적절히 회전시키고 쌓아서, N×N×N크기의 정육면체를 만들려고 한다. 이 정육면체는 탁자위에 있으므로, 5개의 면만 보인다.
# N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.

# n = int(input())
# dice_num = list(map(int, input().split()))

# one_side = min(dice_num)
# two_side = -1
# three_side = -1
# res = 0
# temp = []

# for i in range(0, len(dice_num)-1):
#     for j in range(i+1, len(dice_num)):
#         if i == 0 and j == 5:
#             continue
#         elif i == 1 and j == 4:
#             continue
#         elif i == 2 and j == 3:
#             continue
#         temp.append(dice_num[i]+dice_num[j])
# two_side = min(temp)
# temp.clear()
# temp1 = []
# temp2 = []
# for i in range(1, len(dice_num)-1):
#     for j in range(i+1, len(dice_num)-2):
#         if i == 1 and j == 4:
#             continue
#         elif i == 2 and j == 3:
#             continue
#         temp1.append(dice_num[i]+dice_num[j]+dice_num[0])
#         temp2.append(dice_num[i]+dice_num[j]+dice_num[5])
# temp = temp1 + temp2
# three_side = min(temp)

# if n == 1:
#     dice_num.sort(reverse=True)
#     dice_num.pop()
#     res = sum(dice_num)
# else:
#     res = two_side*((8*n)-12) + three_side*4 + one_side*(4*((n-2)*(n-1)) + (n-2)**2)
# print(res)
# 이건 왜 틀렸을까..


import sys

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, sys.stdin.readline().split()))
    ans = 0
    min_lists = []
    if N == 1:
        arr.sort()
        for i in range(5):
            ans += arr[i]
    else:
        min_lists.append(min(arr[0], arr[5]))
        min_lists.append(min(arr[1], arr[4]))
        min_lists.append(min(arr[2], arr[3]))
        min_lists.sort()

        # 1, 2, 3 면의 주사위 최소값
        min1 = min_lists[0]
        min2 = min_lists[0] + min_lists[1]
        min3 = sum(min_lists)

        # 1, 2, 3 면의 주사위 개수
        n1 = 4 * (N - 2) * (N - 1) + (N - 2) ** 2
        n2 = 4 * (N - 1) + 4 * (N - 2)
        n3 = 4

        ans += min1 * n1
        ans += min2 * n2
        ans += min3 * n3
    print(ans)