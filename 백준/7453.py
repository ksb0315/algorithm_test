# 정수로 이루어진 크기가 같은 배열 A, B, C, D가 있다.
# A[a], B[b], C[c], D[d]의 합이 0인 (a, b, c, d) 쌍의 개수를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
aarr = []
barr = []
carr = []
darr = []
res = 0

for _ in range(n):
    a, b, c, d = map(int, input().split())
    aarr.append(a)
    barr.append(b)
    carr.append(c)
    darr.append(d)

ab = dict()
for a in aarr:
    for b in barr:
        v = a + b
        if v not in ab.keys():
            ab[v] = 1
        else:
            ab[v] += 1


for c in carr:
    for d in darr:
        v = -1 * (c + d)
        if v in ab.keys():
            res += ab[v]

print(res)
