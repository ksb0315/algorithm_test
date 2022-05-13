# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.
# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

n = int(input())
qu = [0 for _ in range(n)]
cnt = 0

def is_promising(x):
    for i in range(x):
        if qu[x] == qu[i] or abs(qu[x]-qu[i]) == abs(x-i):
            return False
    return True
    
def queen(x):
    global cnt
    if x == n:
        cnt += 1
        return
    for i in range(n):
        qu[x] = i
        if is_promising(x):
            queen(x+1)

queen(0)
print(cnt)