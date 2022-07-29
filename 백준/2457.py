# 오늘은 공주님이 태어난 경사스러운 날이다. 왕은 이 날을 기념하기 위해 늘 꽃이 피어있는 작은 정원을 만들기로 결정했다.
# 총 N개의 꽃이 있는 데, 꽃은 모두 같은 해에 피어서 같은 해에 진다. 하나의 꽃은 피는 날과 지는 날이 정해져 있다. 예를 들어, 5월 8일 피어서 6월 13일 지는 꽃은 5월 8일부터 6월 12일까지는 꽃이 피어 있고, 6월 13일을 포함하여 이후로는 꽃을 볼 수 없다는 의미이다. (올해는 4, 6, 9, 11월은 30일까지 있고, 1, 3, 5, 7, 8, 10, 12월은 31일까지 있으며, 2월은 28일까지만 있다.)
# 이러한 N개의 꽃들 중에서 다음의 두 조건을 만족하는 꽃들을 선택하고 싶다.
# 공주가 가장 좋아하는 계절인 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 한다.
# 정원이 넓지 않으므로 정원에 심는 꽃들의 수를 가능한 적게 한다. 
# N개의 꽃들 중에서 위의 두 조건을 만족하는, 즉 3월 1일부터 11월 30일까지 매일 꽃이 한 가지 이상 피어 있도록 꽃들을 선택할 때, 선택한 꽃들의 최소 개수를 출력하는 프로그램을 작성하시오. 
import sys

input = sys.stdin.readline
n = int(input())
date = []

for _ in range(n):
    temp = list(map(int, input().split()))
    date.append([temp[0] * 100 + temp[1], temp[2] * 100 + temp[3]])

date.sort(key=lambda x:(x[0], x[1]))
cnt = 0
end = 0
target = 301

while date:
    if target >= 1201 or target < date[0][0]:
        break

    for _ in range(len(date)):
        if target >= date[0][0]:
            if end <= date[0][1]:
                end = date[0][1]

            date.remove(date[0])

        else:
            break

    target = end
    cnt += 1

if target < 1201:
    print(0)
else:
    print(cnt)
    
