# 연세대학교 수강신청이 얼마 전부터 바뀌어, 마일리지 제도로 바뀌었다. 이 제도는 각각의 학생들에게 마일리지를 주어 듣고 싶은 과목에 마일리지를 과목당 1~36을 분배한다. 그리고 모두 분배가 끝이 나면 과목에 대해서 마일리지를 많이 투자한 순으로 그 과목의 수강인원만큼 신청되는 방식이다.
# 성준이는 연세대학교 재학 중인 학생이다. 성준이는 저번 수강신청에서 실패하여 휴학을 했기 때문에 이번 수강신청만은 필사적으로 성공하려고 한다. 그래서 성준이는 학교 홈페이지를 뚫어버렸다.
# 그 덕분에 다른 사람들이 신청한 마일리지를 볼 수 있게 되었다. 성준이는 주어진 마일리지로 최대한 많은 과목을 신청하고 싶어 한다. (내가 마일리지를 넣고 이후에 과목을 신청하는 사람은 없다) 마일리지는 한 과목에 1에서 36까지 넣을 수 있다.

import heapq

ans = 0
n, m = map(int, input().split())
temp = []

for _ in range(n):
    P, L = map(int, input().split())
    mileages = list(map(int, input().split()))
    heapq.heapify(mileages)
    num = L - P
    # 수강미달인 과목
    if num > 0:
        heapq.heappush(temp, 1)
    else:
        for i in range(abs(num)):
            heapq.heappop(mileages)
        # 수강가능한 마일리지 중 가장 낮은 마일리지 (점수가 동일하다면 성준이에게 우선순위가 있기때문)    
        heapq.heappush(temp, heapq.heappop(mileages))

while temp:
    mileage = heapq.heappop(temp)
    if m - mileage >= 0:
        ans+=1
        m-= mileage
    else:
        break

print(ans) 