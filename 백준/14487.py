# N개의 스위치와 N개의 전구가 있다. 각각의 전구는 켜져 있는 상태와 꺼져 있는 상태 중 하나의 상태를 가진다. i(1 < i < N)번 스위치를 누르면 i-1, i, i+1의 세 개의 전구의 상태가 바뀐다. 즉, 꺼져 있는 전구는 켜지고, 켜져 있는 전구는 꺼지게 된다. 1번 스위치를 눌렀을 경우에는 1, 2번 전구의 상태가 바뀌고, N번 스위치를 눌렀을 경우에는 N-1, N번 전구의 상태가 바뀐다.
# N개의 전구들의 현재 상태와 우리가 만들고자 하는 상태가 주어졌을 때, 그 상태를 만들기 위해 스위치를 최소 몇 번 누르면 되는지 알아내는 프로그램을 작성하시오.

from sys import stdin
import copy

N = int(stdin.readline())
A = list(map(int, stdin.readline().rstrip()))
B = list(map(int, stdin.readline().rstrip()))

r1 = copy.deepcopy(A)
r2 = copy.deepcopy(A)


def two_flip(i, j):
    A[i] = 1 - A[i]
    A[j] = 1 - A[j]


def three_flip(i, j, k):
    A[i] = 1 - A[i]
    A[j] = 1 - A[j]
    A[k] = 1 - A[k]


for i in range(2):
    A = r1 if i == 0 else r2

    cnt = 0
    for j in range(N):
        if j == 0:
            if i == 0 and A != B:
                cnt += 1
                two_flip(j, j+1)

        elif 1 <= j <= N-2:
            if A[j-1] != B[j-1]:
                cnt += 1
                three_flip(j-1, j, j+1)

        elif j == N-1:
            if A[j-1] != B[j-1]:
                cnt += 1
                two_flip(j-1, j)

    if A == B:
        print(cnt)
        break

if A != B:
    print(-1)