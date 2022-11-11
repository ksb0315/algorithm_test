# 수현이는 일년의 날짜가 1일부터 365일로 표시되어있는 달력을 가지고있다. 수현이는 너무나도 계획적인 사람이라 올 해 일정을 모두 계획해서 달력에 표시해놨다. 
# 여름이 거의 끝나가자 장마가 시작되었고, 습기로 인해 달력에 표시한 일정이 지워지려고 한다. 지워지는 것을 막고자 수현이는 일정이 있는 곳에만 코팅지를 달력에 붙이려고 한다. 하지만 너무 귀찮았던 나머지, 다음과 같은 규칙을 따르기로 한다.
# 연속된 두 일자에 각각 일정이 1개 이상 있다면 이를 일정이 연속되었다고 표현한다.
# 연속된 모든 일정은 하나의 직사각형에 포함되어야 한다. 
# 연속된 일정을 모두 감싸는 가장 작은 직사각형의 크기만큼 코팅지를 오린다.
# 달력은 다음과 같은 규칙을 따른다.
# 일정은 시작날짜와 종료날짜를 포함한다.
# 시작일이 가장 앞선 일정부터 차례대로 채워진다.
# 시작일이 같을 경우 일정의 기간이 긴 것이 먼저 채워진다.
# 일정은 가능한 최 상단에 배치된다.
# 일정 하나의 세로의 길이는 1이다. 
# 하루의 폭은 1이다. 
# 위의 그림에서와 같이 일정이 주어졌다고 하자. 여기서 코팅지의 면적은 아래의 파란색 영역과 같다.
# 이때 코팅지의 크기의 합은 3 x 8 + 2 x 2 = 28이다. 
# 일정의 개수와 각 일정의 시작날짜, 종료날짜가 주어질 때 수현이가 자르는 코팅지의 면적을 구해보자.

import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, y+1):
        arr.append(i)

cal = [0] * (max(arr)+2)
width = 0
start_ind = []
end_ind = []

for i in range(max(arr)+2):
    cal[i] += arr.count(i)
    if cal[i] != 0:
        width += 1
        if width == 1:
            start_ind.append(i)
    else:
        if width != 0:
            end_ind.append(i)
        width = 0

ans = 0
for i in range(len(start_ind)):
    ans += (max(cal[start_ind[i] : end_ind[i]]) * (end_ind[i] - start_ind[i]))

print(ans)
