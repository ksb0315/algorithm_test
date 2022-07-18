# 세준이는 동전 뒤집기를 하려고 한다. 세준이는 동전을 N×M개 가지고 있다. 동전은 세로로 N개, 가로로 M개 크기의 직사각형에 차곡차곡 놓여져 있다.
# 동전의 앞면을 0이라고 하고 뒷면을 1이라고 했을 때, 세준이는 모든 동전을 뒤집어서 앞면으로 만들려고 한다.
# 세준이가 (a,b)칸을 뒤집으려고 한다면, (i,j) (1 ≤ i ≤ a, 1 ≤ j ≤ b)의 조건을 만족하는 a×b개의 동전이 한번에 모두 뒤집힌다. (i는 위에서부터 위치의 위치이고, j는 왼쪽에서 부터의 위치이다.)
# 세준이가 뒤집어야하는 동전의 개수를 출력하시오. (a,b)칸을 선택해서 a×b개가 뒤집혔다면, 동전을 뒤집은 횟수는 a×b가 아니라 1이다.

import sys

input = sys.stdin.readline

def xor(a, b):
    for row in range(a + 1):
        for col in range(b + 1):
            matrix[row][col] ^= 1

n, m = map(int, input().split())
matrix = [list(map(int, list(input().rstrip()))) for __ in range(n)]
cnt = 0
for row in range(n - 1, -1, -1):
    for col in range(m - 1, -1, -1):
        if matrix[row][col]:
            cnt += 1
            xor(row, col)
print(cnt)