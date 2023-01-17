
import sys

input = sys.stdin.readline

data = [[0] * 26 for _ in range(26)]

keyborad = {
    'Q' : (0, 0, 0),
    'W' : (0, 4, 1),
    'E' : (0, 8, 2),
    'R' : (0, 12, 3),
    'T' : (0, 16, 4),
    'Y' : (0, 20, 5),
    'U' : (0, 24, 6),
    'I' : (0, 28, 7),
    'O' : (0, 32, 8),
    'P' : (0, 36, 9),
    'A' : (4, 1, 10),
    'S' : (4, 5, 11),
    'D' : (4, 9, 12),
    'F' : (4, 13, 13),
    'G' : (4, 17, 14),
    'H' : (4, 21, 15),
    'J' : (4, 25, 16),
    'K' : (4, 29, 17),
    'L' : (4, 33, 18),
    'Z' : (8, 3, 19),
    'X' : (8, 7, 20),
    'C' : (8, 11, 21),
    'V' : (8, 15, 22),
    'B' : (8, 19, 23),
    'N' : (8, 23, 24),
    'M' : (8, 27, 25)
}

for i, (key_i, value_i) in enumerate(keyborad.items()):
    for j, (key_j, value_j) in enumerate(keyborad.items()):
        data[i][j] = (value_i[0] - value_j[0]) * (value_i[0] - value_j[0]) + (value_i[1] - value_j[1]) * (value_i[1] - value_j[1])

def dist(ind):
    b = len(words[ind])
    table = [[0] * (b+1) for _ in range(l+1)]
    for i in range(1,len(table[0])):
        table[0][i] = 1600 * i
    for i in range(1, len(table)):
        table[i][0] = 1600 * i
    for i in range(1, l+1):
        for j in range(1, b+1):
            point = data[keyborad[wrong[i - 1]][2]][keyborad[words[ind][j - 1]][2]]
            table[i][j] = min([table[i-1][j-1] + point, table[i - 1][j] + 1600, table[i][j - 1] + 1600])
    return table[l][b]

n = int(input())
mini = float('inf')
ans = []
ans_ind = []
words = []

for _ in range(n):
    words.append(input().rstrip())

wrong = input().rstrip()
l = len(wrong)
for i in range(n):
    res = dist(i)
    if res < mini:
        mini = res
        ans_ind = []
        ans_ind.append(i)
        continue
    elif res == mini:
        ans_ind.append(i)

for i in range(len(ans_ind)):
    ans.append(words[ans_ind[i]])

ans.sort()
for a in ans:
    print(a)