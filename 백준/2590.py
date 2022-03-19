# <그림 1>과 같이 정사각형 모양을 한 여섯 종류의 색종이가 있다. 1번 색종이는 한 변의 길이가 1cm이고, 차례대로 그 길이가 1cm씩 커져, 6번 색종이의 한 변의 길이는 6cm가 된다.
# 주어진 색종이를 <그림 2>와 같이 가로, 세로의 길이가 각각 6cm인 판 위에 붙이려고 한다. 색종이를 붙일 때는 색종이가 판의 경계 밖으로 삐져 나가서는 안되며, 색종이가 서로 겹쳐서도 안 된다. 또한 하나의 색종이는 하나의 판에만 붙여야 한다.
# 각 종류별로 색종이의 장수가 주어질 때, 그 색종이를 모두 붙이기 위해서 위와 같은 판이 최소 몇 개가 필요한지 구하는 프로그램을 작성하시오.

paper = [0]
ans = 0
for _ in range(6):
    paper.append(int(input()))

if paper[6]:
    ans += paper[6]

while paper[5]:
    area = 36 - 5*5
    paper[5] -= 1
    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[4]:
    area = 36 - 4*4
    area -= min(paper[2], 5) * 4
    paper[4] -= 1
    paper[2] = max(paper[2]-5, 0)
    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[3]:
    area = 36 - 9 * min(paper[3], 4)
    if paper[3] >= 4:
        paper[3] -= 4
        area = 0
    elif paper[3] == 3:
        area -= min(1, paper[2]) * 4
        paper[3] -= 3
        paper[2] = max(paper[2]-1, 0)
    elif paper[3] == 2:
        area -= min(3, paper[2]) * 4
        paper[3] -= 2
        paper[2] = max(paper[2]-3, 0)
    else:
        area -= min(5, paper[2]) * 4
        paper[3] -= 1
        paper[2] = max(paper[2]-5, 0)

    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[2]:
    area = 36 - 4 * min(paper[2], 9)
    paper[2] = max(paper[2]-9, 0)
    paper[1] = max(paper[1]-area, 0)
    ans += 1

while paper[1]:
    paper[1] = max(paper[1]-36, 0)
    ans += 1

print(ans)