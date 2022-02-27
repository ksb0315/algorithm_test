# 정수 N과 K가 주어졌을 때, 다음 두 조건을 만족하는 문자열 S를 찾는 프로그램을 작성하시오.
#   문자열 S의 길이는 N이고, 'A', 'B'로 이루어져 있다.
#   문자열 S에는 0 ≤ i < j < N 이면서 s[i] == 'A' && s[j] == 'B'를 만족하는 (i, j) 쌍이 K개가 있다.

n , k = map(int,input().split())

def check(word):
    cnt = 0
    for i in range(len(word)-1):
        if word[i] == 'A':
            for j in range(i+1,len(word)):
                if word[j] == 'B':
                    cnt += 1
    return cnt

a = 'B'*n
a = list(a)
for i in range(n):
    a[i] = 'A'
    c= check(a)
    if c == k:
        break
    elif c > k:
        a[i] = 'B'

t = "".join(a)
if t=='B'*n or t=='A'*n:
    if k == 0:
        print(t)
    else:
        print(-1)
else:
    print(t)