# 각 마을은 배송할 물건들을 박스에 넣어 보내며, 본부에서는 박스를 보내는 마을번호, 박스를 받는 마을번호와 보낼 박스의 개수를 알고 있다. 박스들은 모두 크기가 같다. 트럭에 최대로 실을 수 있는 박스의 개수, 즉 트럭의 용량이 있다. 이 트럭 한대를 이용하여 다음의 조건을 모두 만족하면서 최대한 많은 박스들을 배송하려고 한다.
#   조건 1: 박스를 트럭에 실으면, 이 박스는 받는 마을에서만 내린다.
#   조건 2: 트럭은 지나온 마을로 되돌아가지 않는다.
#   조건 3: 박스들 중 일부만 배송할 수도 있다.
# 마을의 개수, 트럭의 용량, 박스 정보(보내는 마을번호, 받는 마을번호, 박스 개수)가 주어질 때, 트럭 한 대로 배송할 수 있는 최대 박스 수를 구하는 프로그램을 작성하시오. 단, 받는 마을번호는 보내는 마을번호보다 항상 크다.

import sys

n, c = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

box.sort(key=lambda x:x[1])  # 도착 시간이 빠른 순서로 정렬

answer = 0  # 최대 박스 수
remain = [c] * (n + 1)  # 각 위치에 남은 공간

for i in range(m):
    temp = c  # c개를 옮길 수 있다고 가정
    for j in range(box[i][0], box[i][1]):
        temp = min(temp, remain[j])
    temp = min(temp, box[i][2])
    for j in range(box[i][0], box[i][1]):
        remain[j] -= temp
    answer += temp

print(answer)