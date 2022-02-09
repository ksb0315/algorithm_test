# 오늘은 공주님이 태어난 경사스러운 날이다. 왕은 이 날을 기념하기 위해 늘 꽃이 피어있는 작은 정원을 만들기로 결정했다.
# 총 N개의 꽃이 있는 데, 꽃은 모두 같은 해에 피어서 같은 해에 진다. 하나의 꽃은 피는 날과 지는 날이 정해져 있다. 예를 들어, 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미이다. (올해는 4, 6, 9, 11월은 30일까지 있고, 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며, 2월은 28일까지만 있다.)
# 이러한 N개의 꽃들 중에서 다음의 두 조건을 만족하는 꽃들을 선택하고 싶다.
# 공주가 가장 좋아하는 계절인 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
# 정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다. 
# N개의 꽃들 중에서 위의 두 조건을 만족하는, 즉 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 꽃들을 선택할 때, 선택한 꽃들의 최소 개수를 출력하는 프로그램을 작성하시오. 

from sys import stdin
from collections import deque
import datetime
input = stdin.readline

n = int(input())
flowers = []
# start month, day & end month, day
for i in range(n):
    start_month, start_day, end_month, end_day = map(int, input().split())
    a = datetime.date(1999, start_month, start_day)
    b = datetime.date(1999, end_month, end_day)
    flowers.append((a, b))

# 시작 날짜를 기준으로 정렬하기 -> 만약 같은 날짜에 시작한다면, 일찍 끝나는 꽃이 우선적으로 정렬
sorted_flowers = deque(sorted(flowers, key=lambda x : (x[0], x[1])))

result = []
flag = True

# 가장 긴걸 뽑기
# 겹치는 시간 최소화
# 3/1 ~ 12/1 신경쓰기
while sorted_flowers:
    start, end = sorted_flowers.popleft()
    if len(result) == 0:
        if start <= datetime.date(1999, 3, 1):
            result.append((start, end))
        else:
            flag = False
            break
    else:
        pre_start, pre_end = result.pop()
        if pre_end > end:       # 이전 꽃이 더 늦게 질 때
            result.append((pre_start, pre_end))
        else:                   # 이전 꽃이 더 빨리 질 때
            if start <= datetime.date(1999, 3, 1):
                result.append((start, end))
            elif pre_end >= datetime.date(1999, 12, 1): # 이미 result의 마지막 원소로 11/30을 포함할 때
                if len(result) == 0:
                    result.append((pre_start, pre_end))                    
                else:
                    before_start, before_end = result.pop() 
                    if start > pre_start and before_end >= pre_start:
                        result.append((before_start, before_end))
                        result.append((start, end))
                    else:
                        result.append((before_start, before_end))
                        result.append((pre_start, pre_end))                    
            else:   # 3/1, 11/30에 걸치지 않을 때
                if len(result) == 0:    # 남는거 없으면 그냥 넣기(비교대상이 없으므로)
                    result.append((pre_start, pre_end))
                    result.append((start, end))
                else:                   # 남는게 있는 경우
                    before_start, before_end = result.pop()     # 그 전 전 원소 뽑기
                    if before_end >= start:                     # 그 전 전 꽃이 현재 꽃의 시작보다 늦게 질 때 (포함하는 경우) ~ 겹치는 시간 최소화
                        result.append((before_start, before_end))
                        result.append((start, end))   
                    else:                                       # 그 전 전 꽃이 현재 꽃의 시작보다 빨리 질 때 (포함 못함)
                        result.append((before_start, before_end))
                        result.append((pre_start, pre_end))
                        result.append((start, end))                                        
if flag:
    if result[-1][1] <= datetime.date(1999, 11, 30): # 마지막 원소가 11월 30일을 포함하지 않는 경우
        print(0)
    else:
        print(len(result))
else:
    print(0)



#아직 못품
#다음기회에..
