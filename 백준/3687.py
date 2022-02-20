# 성냥개비는 숫자를 나타내기에 아주 이상적인 도구이다. 보통 십진수를 성냥개비로 표현하는 방법은 다음과 같다.
# 성냥개비의 개수가 주어졌을 때, 성냥개비를 모두 사용해서 만들 수 있는 가장 작은 수와 큰 수를 찾는 프로그램을 작성하시오.

import sys
input=sys.stdin.readline

t=int(input())
result = []
for _ in range(t):
    n=int(input())
    match=[6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    ans=[0, 0, 1, 7, 4, 2, 6, 8, 10, 18, 22]
    ansMax='7'*(n%2)+'1'*(n//2-(n%2))
    if n<=10: 
        result.append([ans[n],ansMax])
        continue

    ansMin=''
    while n>0:
        n-=7
        if n>=0: ansMin+='8'
        else: n+=7; break

    small={6:6, 2:1, 5:2}
    if n in small: ansMin=str(small[n])+ansMin
    else: 
        if n==1: ansMin='10'+ansMin[1:]
        elif n==3: ansMin='200'+ansMin[2:]
        elif n==4: ansMin='20'+ansMin[1:]
    result.append([ansMin,ansMax])

for i in range(t):
    print(result[i][0], result[i][1])