# 아 과제 하기 싫다. 아무 것도 안 하고 싶다. 더 적극적이고 격렬하게 아무 것도 안 하고 싶다.
# 있잖아. 내가 아까 책상에다가 n개의 과제 목록을 적어놨어. 각각의 과제 i는 di 일이 걸리고, 오늘로부터 ti 일 안에 끝내야 해. 그러니까 오늘이 0일이면, ti일이 끝나기 전에 제출이야. 과제는 한번 시작하면 쉬지 않고 계속해야 해. 안 그러면 머리 아파 지거든.
# 근데 있잖아. 내가 지금 너무, 너무 아무 것도 안 하고 싶어. 그래서 오늘은 아무 것도 안 할 거야. 더 중요한 게 뭔지 알아? 사실 나 내일도, 모레도, 아무 것도 안 하고 싶어. 한 며칠 동안은 계속 아무 것도 안하려고. 아. 과제가 있을 때 내가 내일부터 연속으로 최대 며칠동안 놀 수 있는지 궁금하다. 궁금하긴 한데, 난 아무 것도 안 하고 싶어.
# 좋은 생각이 났다. 너희가 이걸 대신 구해주면, 내가 너희의 맞은 문제 수를 하나 올려줄게

import sys
input = sys.stdin.readline
n = int(input())
work = [list(map(int, input().split())) for _ in range(n)]
work.sort(key=lambda x: x[1], reverse = True)
spare_time = work[0][1]
for i in range(n):
    spare_time = min(work[i][1], spare_time) - work[i][0]
print(spare_time)