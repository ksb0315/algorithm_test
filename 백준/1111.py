# IQ Test의 문제 중에는 공통된 패턴을 찾는 문제가 있다. 수열이 주어졌을 때, 다음 수를 찾는 문제이다.
# 예를 들어, 1, 2, 3, 4, 5가 주어졌다. 다음 수는 무엇인가? 당연히 답은 6이다. 약간 더 어려운 문제를 보면, 3, 6, 12, 24, 48이 주어졌을 때, 다음 수는 무엇인가? 역시 답은 96이다.
# 이제 제일 어려운 문제를 보자.
# 1, 4, 13, 40이 주어졌을 때, 다음 수는 무엇일까? 답은 121이다. 그 이유는 항상 다음 수는 앞 수*3+1이기 때문이다.
# 은진이는 위의 3문제를 모두 풀지 못했으므로, 자동으로 풀어주는 프로그램을 작성하기로 했다. 항상 모든 답은 구하는 규칙은 앞 수*a + b이다. 그리고, a와 b는 정수이다.
# 수 N개가 주어졌을 때, 규칙에 맞는 다음 수를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))

if n == 1:
    print("A")
elif n == 2:
    if arr[0] == arr[1]:
        print(arr[0])
    else:
        print("A")
else:
    if arr[0] - arr[1] == 0:
        a = 0
    else:
        a = (arr[1] - arr[2]) // (arr[0] - arr[1])
    b = arr[1] - arr[0] * a

    for i in range(n-1):
        expect = arr[i] * a + b
        if arr[i + 1] != expect:
            print('B')
            exit()
    
    print(arr[-1] * a + b)
