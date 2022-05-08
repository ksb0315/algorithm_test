# 밑변이 모두 x축에 평행한 N개의 직사각형이 주어질 때, 이 N개의 직사각형들이 차지하는 면적을 구하는 프로그램을 작성하시오. 여기서 주어진 직사각형들은 서로 겹칠 수도 있으며, 변이나 꼭짓점을 공유할 수도 있다.


def count(list):
    cnt = 0
    for e in list:
        if e != 0:
            cnt += 1
    return cnt


n = int(input())
rec = []
for __ in range(n):
    x, y, w, h = map(float, input().split())
    rec.append([x, y, y+h, 1])
    rec.append([x+w, y, y+h, -1])

rec.sort()

area = 0
ylist = [0]*25001

for i in range(len(rec)-1):
    x, y1, y2, flag = rec[i]
    y1 = int(y1*10)
    y2 = int(y2*10)
    if flag == 1:
        for j in range(y1, y2):
            ylist[j] += 1
    if flag == -1:
        for j in range(y1, y2):
            ylist[j] -= 1
    area += (rec[i+1][0] - x)*count(ylist)/10

if area-int(area) > 0:
    print(f'{area:0.2f}')
else:
    print(int(area))