# 정렬되어있는 두 배열 a와 b가 주어진다. 두 배열을 합친 다음 정렬해서 출력하는 프로그램을 작성하시오.

import sys

input = lambda: sys.stdin.readline()

n, m = map(int, input().split())

a_arr = list(map(int, input().split()))
b_arr = list(map(int, input().split()))
answer = []

a_pointer, b_pointer = 0, 0
a_length, b_length = len(a_arr), len(b_arr)

while a_pointer != a_length or b_pointer != b_length:
    if a_pointer == a_length:
        answer.append(b_arr[b_pointer])
        b_pointer += 1
    elif b_pointer == b_length:
        answer.append(a_arr[a_pointer])
        a_pointer += 1
    else:
        if a_arr[a_pointer] < b_arr[b_pointer]:
            answer.append(a_arr[a_pointer])
            a_pointer += 1
        else:
            answer.append(b_arr[b_pointer])
            b_pointer += 1

print(*answer)