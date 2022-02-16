# 웅찬이는 과제가 많다. 하루에 한 과제를 끝낼 수 있는데, 과제마다 마감일이 있으므로 모든 과제를 끝내지 못할 수도 있다. 과제마다 끝냈을 때 얻을 수 있는 점수가 있는데, 마감일이 지난 과제는 점수를 받을 수 없다.
# 웅찬이는 가장 점수를 많이 받을 수 있도록 과제를 수행하고 싶다. 웅찬이를 도와 얻을 수 있는 점수의 최댓값을 구하시오.

n = int(input()) #과제수
homework = []
for _ in range(n):
    x, y = map(int, input().split())
    homework.append((x,y))
homework.sort()

can    = []
date   = homework[-1][0]
answer = 0

while True:
    if date == 0:
        break
    while homework and homework[-1][0] >= date:
        can.append(homework.pop()[1])
    date -= 1
    if not can:
        continue
    can.sort()
    answer += can.pop()
print(answer)