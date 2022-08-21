# N개의 영단어들이 주어졌을 때, 가장 비슷한 두 단어를 구해내는 프로그램을 작성하시오.
# 두 단어의 비슷한 정도는 두 단어의 접두사의 길이로 측정한다. 접두사란 두 단어의 앞부분에서 공통적으로 나타나는 부분문자열을 말한다. 즉, 두 단어의 앞에서부터 M개의 글자들이 같으면서 M이 최대인 경우를 구하는 것이다. "AHEHHEH", "AHAHEH"의 접두사는 "AH"가 되고, "AB", "CD"의 접두사는 ""(길이가 0)이 된다.
# 접두사의 길이가 최대인 경우가 여러 개일 때에는 입력되는 순서대로 제일 앞쪽에 있는 단어를 답으로 한다. 즉, 답으로 S라는 문자열과 T라는 문자열을 출력한다고 했을 때, 우선 S가 입력되는 순서대로 제일 앞쪽에 있는 단어인 경우를 출력하고, 그런 경우도 여러 개 있을 때에는 그 중에서 T가 입력되는 순서대로 제일 앞쪽에 있는 단어인 경우를 출력한다.

import sys

input = sys.stdin.readline

n = int(input())
a = [input().rstrip() for _ in range(n)]

b = sorted(list(enumerate(a)),key = lambda x: x[1])

def check(a, b):
    cnt = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]: cnt += 1
        else: break
    return cnt

length = [0] * (n+1)
maxlength = 0

for i in range(n-1):
    tmp = check(b[i][1], b[i+1][1])
    maxlength = max(maxlength, tmp)

    length[b[i][0]] = max(length[b[i][0]], tmp)
    length[b[i+1][0]] = max(length[b[i+1][0]], tmp)
    
first = 0
for i in range(n):
    if first == 0:
        if length[i] == max(length):
            first = a[i]
            print(first)
            pre = a[i][:maxlength]
    else:
        if length[i] == max(length) and a[i][:maxlength] == pre:
            print(a[i])
            break
