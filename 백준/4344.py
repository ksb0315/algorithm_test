# 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.

import sys

input = sys.stdin.readline

case = int(input())
for _ in range(case):
    scores = list(map(int, input().split()))
    m = sum(scores[1:])/scores[0]
    cnt = 0
    for i in range(1, scores[0]+1):
        if scores[i] > m:
            cnt += 1
    print("{0:0.3f}%".format(round((cnt/scores[0]) * 100, 3)))
