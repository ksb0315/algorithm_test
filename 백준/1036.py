# 36진법의 숫자는 0부터 9까지의 수와 알파벳 A에서 Z로 나타낸다. A부터 Z까지 알파벳은 10부터 35에 차례대로 대응한다.
# 36진법의 수 N개가 주어진다. 36진법 숫자(0-9, A-Z) 중에서 K개의 숫자를 고른다. 그러고 나서 N개의 수 모두에서 나타난 그 숫자를 Z로 바꾼다. 그 이후에 N개의 수를 모두 더한다.
# 이때 가능한 합의 최댓값을 구하는 프로그램을 작성하시오. 합의 최댓값도 36진수로 출력한다.
def f(n):
    q = n // 36
    r = n % 36
    if q:
        if 0<=r<=9:
            return f(q) + chr(r+48) 
        else:
            return f(q) + chr(r+55)
    else:
        if 0<=r<=9:
            chr(r+48) 
        else:
            chr(r+55)


    return f(q) + (chr(r+48) if 0 <= r <= 9 else chr(r+55)) if q else chr(r+48) if 0<= r <=9 else chr(r+55)
N = int(input())
c = [0]*36
for i in range(N):
    n = input()
    l = len(n)
    for j in range(l):
        c[int(n[j],36)] += 36**(l-j-1)
K = int(input())
A = [[c[i]*(35-i), i]for i in range(36)]
A.sort()
s=0
for i in range(36):
    if i < 36-K:
        s+=c[A[i][1]] * A[i][1] 
    else:
        s+=c[A[i][1]] * 35   
    
print(f(s))

