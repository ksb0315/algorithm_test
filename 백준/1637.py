#동물원에서 막 탈출한 원숭이 한 마리가 세상구경을 하고 있다. 그 원숭이는 좀 특이한 원숭이였다. 어떤 것도 꿰뚫어볼 수 있는 날카로운 눈을 가진 기이한 원숭이였다. 부드러운 눈을 가진 멍멍이는 언제나 날카로운 눈을 가진 원숭이를 부러워했지만 한편으로는 매우 질투했다.
#어느 날 멍멍이는 원숭이의 날카로운 눈이 너무 샘나서 원숭이를 직접 패고 싶었지만 날카로운 눈으로 찌를까봐 무서워서 때리지는 못하고 대신, 원숭이에게 문제 하나를 던져주었다. 그 문제는 다음과 같다.
#정수가 여러 개 모여 있는 정수더미가 있다. 그 안에 어떤 특정한 정수 하나만 홀수개 존재하고 나머지 정수는 모두 짝수개 존재한다. 정수더미 속에서 날카로운 눈을 이용해 홀수개 존재하는 정수를 찾아야 하는 문제이다.
#근데 멍멍이가 문제를 전달해 주려다가 생각해보니 정수더미 안에 정수가 적게 있으면 문제가 너무 쉬워지게 되는 것이다. 그래서 정수더미안에 정수를 무지막지하게 많이 넣기로 했다. 정수더미가 주어졌을 때, 그 안에 홀수개 존재하는 정수를 찾는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

def get_sum(target):
    total = 0
    for i in range(n):
        if target >= arr[i][0]:
            total += ((min(arr[i][1],target) - arr[i][0])//arr[i][2]) + 1
    return total

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
left = 0
right = 2147483648
while left < right:
    mid = (left + right)//2
    if not get_sum(mid)&1:
        left = mid + 1
    else:
        right = mid
if left == 2147483648:
    print('NOTHING')
else:
    print(left,get_sum(left) - get_sum(left-1))