# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오. 

import sys

input = sys.stdin.readline

n = int(input())

if n < 100:
    print(n)
else:
    cnt = 99
    for num in range(100,n+1):
        str_n = str(num)
        flag = False
        for i in range(len(str_n)-1):
            j = i+1
            if flag:
                if temp == int(str_n[j]) - int(str_n[i]):
                    cnt += 1
                else:
                    break
            else:
                temp = int(str_n[j]) - int(str_n[i])
                flag = True
    print(cnt)
