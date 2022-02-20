# 빨간색 볼과 파란색 볼이 <그림 1>에서 보인 것처럼 일직선상에 섞여 놓여 있을 때, 볼을 옮겨서 같은 색 볼끼리 인접하게 놓이도록 하려고 한다. 볼을 옮기는 규칙은 다음과 같다.
#   1.바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길 수 있다. 즉, 빨간색 볼은 옆에 있는 파란색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다. 유사하게, 파란색 볼은 옆에 있는 빨간색 볼 무더기를 한 번에 뛰어 넘어 옮길 수 있다.
#   2.옮길 수 있는 볼의 색깔은 한 가지이다. 즉, 빨간색 볼을 처음에 옮겼으면 다음에도 빨간색 볼만 옮길 수 있다. 유사하게, 파란색 볼을 처음에 옮겼으면 다음에도 파란색 볼만 옮길 수 있다.
# 일직선상에 놓여 있는 볼에 관한 정보가 주어질 때, 규칙에 따라 볼을 이동하여 같은 색끼리 모으되 최소 이동횟수를 찾는 프로그램을 작성하시오.

import sys

N = int(input())
arr = list(map(str, sys.stdin.readline().rstrip()))
red = arr.count('R')
blue = N - red
ans = min(red, blue)
cnt = 0
for i in range(N):
    if arr[i] != arr[0]: break
    cnt += 1
if arr[0] == 'R': ans = min(ans, red - cnt)
else: ans = min(ans, blue - cnt)
cnt = 0
for i in range(N - 1, -1, -1):
    if arr[i] != arr[N - 1]: break
    cnt += 1
if arr[N - 1] == 'R': ans = min(ans, red - cnt)
else: ans = min(ans, blue - cnt)

print(ans)