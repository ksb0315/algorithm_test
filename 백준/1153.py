# 임의의 자연수가 주어지면, 이를 네 개의 소수의 합으로 분해하는 프로그램을 작성하시오. 예를 들어 38 = 5 + 7 + 13 + 13이 된다.

import sys

def aratos():
    for i in range(2,N+1):
        if isPrime[i]:
            primeL.append(i)
            for j in range(i*i,N+1,i):
                isPrime[j]=0


N=int(input())
isPrime = [1 for i in range(N + 1)]
isPrime[0] = isPrime[1] = 0
primeL = []
aratos()
size=len(primeL)

def goldbach(num):
    for i in range(size):
        for j in range(size):
            sumOfNum=primeL[i]+primeL[j]
            if sumOfNum==num:
                ans.extend([primeL[i],primeL[j]])
                return
            elif sumOfNum>num:
                break


if N<8:
    print(-1)
else:
    if N%2==0:
        ans=[2,2]
        N-=4
        goldbach(N)
        print(*ans)
    else:
        ans=[2,3]
        N-=5
        goldbach(N)
        print(*ans)