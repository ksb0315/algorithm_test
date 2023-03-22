# 벌목꾼 백은진은 나무를 종이 공장에 옮겨야 한다. 하지만, 통나무의 길이가 너무 길어서 트럭에 들어가지 않으므로, 여러개의 조각으로 나누려고 한다.
# 통나무의 길이는 L이고, K개의 위치에서만 자를 수 있다. 통나무를 자를 수 있는 위치가 주어진다. 이 위치는 통나무의 가장 왼쪽에서부터 떨어진 거리이다. 통나무를 자를 수 있는 횟수는 최대 C번이다.
# 통나무의 가장 긴 조각을 작게 만들고, 그 길이를 구해보자.

import sys

input = sys.stdin.readline
l, k, c = map(int, input().split())
pos = [0, *sorted([*map(int, input().split())]), l]
pieces = [pos[idx+1] - pos[idx] for idx in range(k+1)]
longest = max(pieces)

def solve(mid):
    if longest > mid:   
        return 10001, 0
    sums_ = 0
    count = 0
    for piece in pieces[::-1]:
        sums_ += piece  
        if sums_ > mid: 
            sums_ = piece
            count += 1
    return count, sums_ if count == c else pieces[0]

left = 0
right = l
while left <= right:
    mid = (left + right) // 2

    count, front = solve(mid)
    if count <= c:           
        ans_longest = mid
        ans_front = front
        right = mid - 1
    else:
        left = mid + 1

print(ans_longest, ans_front)