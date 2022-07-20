#제 1항과 제 2항을 1이라 하고, 제 3항부터는 앞의 두 항의 합을 취하는 수열을 피보나치(fibonacci) 수열이라고 한다. 예를 들어 제 3항은 2이며, 제 4항은 3이다.
#피보나치 수열의 a번째 항부터 b번째 항까지의 합을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으므로 마지막 아홉 자리만을 구하도록 한다. 즉 1,000,000,000으로 나눈 나머지를 구하면 된다.

import sys

input = sys.stdin.readline

mod = 1000000000
def matrix_mult(A, B):
    temp = [[0, 0],[0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                temp[i][k] += (A[i][j] * B[j][k])
                temp[i][k] %= mod
    return temp

def div_conq_fibo(n):
    matrix = [[0,1],[1,1]]
    if n == 1:
        return matrix
    if n % 2 == 0:
        temp = div_conq_fibo(n//2)
        return matrix_mult(temp, temp)
    else:
        temp = div_conq_fibo(n-1)
        return matrix_mult(temp, matrix)

a, b = map(int,input().split())

fibo_1 = div_conq_fibo(a+1)
fibo_2 = div_conq_fibo(b+2)
ans = (fibo_2[0][1] % mod - fibo_1[0][1] % mod + mod) % mod

print(ans)
