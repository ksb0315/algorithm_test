# 36진법의 숫자는 0부터 9까지의 수와 알파벳 A에서 Z로 나타낸다. A부터 Z까지 알파벳은 10부터 35에 차례대로 대응한다.
# 36진법의 수 N개가 주어진다. 36진법 숫자(0-9, A-Z) 중에서 K개의 숫자를 고른다. 그러고 나서 N개의 수 모두에서 나타난 그 숫자를 Z로 바꾼다. 그 이후에 N개의 수를 모두 더한다.
# 이때 가능한 합의 최댓값을 구하는 프로그램을 작성하시오. 합의 최댓값도 36진수로 출력한다.
import sys

def to_36(N):
    d = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    a, b = N // 36, N % 36
    w =d[b]
    if a!=0:
        return to_36(a) + w  
    else:
        return w

N = int(input())
count=dict()
for i in list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
    count[i]=0
digit = []
for _ in range(N):
    digit.append(sys.stdin.readline().strip())

K=int(input())

for i in digit:
    for j in range(len(i)):
        count[i[::-1][j]] +=36**j
    
for i in count.keys():
    count[i] = count[i] * (35-int(i, 36))
count = sorted(count.items())
count.sort(key=lambda x: -x[1])

for i in count[:K]:
    for j in range(len(digit)):
        digit[j] = digit[j].replace(i[0],"Z")    
s=0
for i in digit:
    s += int(i, 36)

print(to_36(s))