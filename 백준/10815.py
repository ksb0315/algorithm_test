# 숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 가지고 있는지 아닌지를 구하는 프로그램을 작성하시오.

n = int(input())
n_arr = sorted(list(map(int,input().split())))
m = int(input())
m_arr = list(map(int, input().split()))

for i in range(m):
    s = 0
    e = n - 1
    flag = False
    while s <= e:
        mid = (s+e)//2
        if m_arr[i] > n_arr[mid]:
            s = mid + 1
        elif m_arr[i] < n_arr[mid]:
            e = mid - 1
        else:
            flag = True
            print(1)
            break
    if flag == False:
        print(0)
