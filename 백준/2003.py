# N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의 합 A[i] + A[i+1] + … + A[j-1] + A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
right = 1
cnt = 0

while right <= n and right >= left:
    size_ = sum(arr[left:right])
    if size_ == m:
        cnt += 1
        right += 1
    elif size_ < m:
        right += 1
    else:
        left += 1

print(cnt)
