# 어떤 정수 X가 1보다 큰 제곱수로 나누어 떨어지지 않을 때, 그 수를 제곱ㄴㄴ수라고 한다. 
# 제곱수는 정수의 제곱이다. min과 max가 주어지면, min보다 크거나 같고, max보다 작거나 같은 제곱ㄴㄴ수가 몇 개 있는지 출력한다.

import sys

input = sys.stdin.readline

a,b = map(int,input().split())

ans = b-a+1
check = [False]*(b-a+1)
i=2

while i*i <= b:
    sqr = i*i 
    rem = 0 if a%sqr==0 else 1
    j = a//sqr + rem
    while sqr*j <= b:
        if not check[sqr*j-a]:
            check[sqr*j-a]=True
            ans-=1
        j+=1
    i+=1        

print(ans)
