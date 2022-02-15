# L과 R이 주어진다. 이때, L보다 크거나 같고, R보다 작거나 같은 자연수 중에 8이 가장 적게 들어있는 수에 들어있는 8의 개수를 구하는 프로그램을 작성하시오.

l, r = input().split()
llen, rlen = len(l), len(r)
cnt = 0
if llen != rlen:
    print(cnt)
else:
    for i in range(llen):
        if l[i] != r[i]:
            break
        else:
            if l[i] == '8':
                cnt+=1
    print(cnt)