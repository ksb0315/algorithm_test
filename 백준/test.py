import sys


def solve():
    N = int(input())
    count=dict()
    for i in list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
        count[i]=0
    n_list = list()
    for _ in range(N):
        n_list.append(sys.stdin.readline().strip())
    
    K=int(input())

    for i in n_list:
        for j in range(len(i)):
            count[i[::-1][j]] +=36**j
    
    for i in count.keys():
        count[i] = count[i] * (35-int(i, 36))
    count = sorted(count.items())
    count.sort(key=lambda x: -x[1])

    for i in count[:K]:
        for j in range(len(n_list)):
            n_list[j] = n_list[j].replace(i[0],"Z")    
    s=0
    for i in n_list:
        s += int(i, 36)

    print(to_36(s))

def to_36(N):
    d = list("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    a, b = N // 36, N % 36
    w =d[b]
    if a!=0:
        return to_36(a) + w  
    else:
        return w
    
solve()