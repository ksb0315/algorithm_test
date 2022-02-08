# 세준이는 도서관에서 일한다. 도서관의 개방시간이 끝나서 세준이는 사람들이 마구 놓은 책을 다시 가져다 놓아야 한다. 
# 세준이는 현재 0에 있고, 사람들이 마구 놓은 책도 전부 0에 있다. 
# 각 책들의 원래 위치가 주어질 때, 책을 모두 제자리에 놔둘 때 드는 최소 걸음 수를 계산하는 프로그램을 작성하시오. 
# 세준이는 한 걸음에 좌표 1칸씩 가며, 책의 원래 위치는 정수 좌표이다. 책을 모두 제자리에 놔둔 후에는 다시 0으로 돌아올 필요는 없다.
# 그리고 세준이는 한 번에 최대 M권의 책을 들 수 있다.

n, m = map(int, input().split())
point = list(map(int, input().split()))
point.sort()
posi = []
nega = []
dist = 0
for i in range(n):
    if point[i] < 0:
        nega.append(point[i])
    elif point[i] > 0:
        posi.append(point[i])
temp = []
for i in range(0,len(nega),m):
    temp.append(nega[i:i+m])
nega = temp
temp = []
posi.sort(reverse=True)
for i in range(0,len(posi),m):
    temp.append(posi[i:i+m])
posi = temp
if not nega:
    nega.append([0])
if not posi:
    posi.append([0])

if abs(nega[0][0]) > abs(posi[0][0]):
    dist += abs(nega[0][0])
    nega.sort(reverse=True)
    nega.pop()
else:
    dist += posi[0][0]
    posi.sort()
    posi.pop()
for i in range(len(nega)):
    dist+=2*abs(nega[i][0])
for i in range(len(posi)):
    dist+=2*abs(posi[i][0])
print(dist)