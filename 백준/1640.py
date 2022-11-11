# 영식이는 밑에 슈퍼에 가서 매일매일 시도때도 없이 과자를 사먹는다. 그러다보니 자연스럽게 동전이 많아졌다. 민식이가 놀아주지않아서 자연스럽게 왕따가된 영식이는 동전들을 N×M모양으로 배열하고 뒤집는 놀이를 하려고 한다. N과 M은 모두 홀수이다.
# 편의상 동전의 앞면을 0, 뒷면을 1이라고 한다.
# 한번 뒤집기를 할 때, 영식이는 어떤 열과 행 중에 하나를 고를 수 있다. 그리고나서 뒤집는 행동을 할 때는, 고른 열이나 행에 있는 모든 동전을 뒤집어야 한다. 0은 1이 되고 1은 0이 된다는 소리다.
# 영식이는 동전을 열심히 뒤집어서 각 열과 행에있는 1의 개수를 모두 짝수개로 맞추려고 한다.
# 영식이가 동전을 뒤집어야하는 횟수의 최솟값을 출력하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
row_col = [[0]*n, [0]*m]

coins = []
for _ in range(n):
    coins.append(input().rstrip())

for i in range(n):
    for j in range(m):
        if coins[i][j] == '1':
            row_col[0][i] += 1
            row_col[1][j] += 1

cnt1 = 0
for i in range(n):
    if row_col[0][i] % 2 == 1:
        cnt1 += 1

cnt2 = 0
for i in range(m):
    if row_col[1][i] % 2 == 1:
        cnt2 += 1

print(min(cnt1, cnt2))