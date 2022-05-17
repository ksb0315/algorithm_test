# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

n = int(input())
A = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))
A.sort()

for num in arr:
    lt, rt = 0, n - 1
    flag = False

    while lt <= rt:
        mid = (lt + rt) // 2
        if num == A[mid]:
            flag = True
            print(1)
            break
        elif num > A[mid]:
            lt = mid + 1
        else:
            rt = mid - 1

    if not flag:
        print(0)