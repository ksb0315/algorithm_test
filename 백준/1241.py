# 엄지 생일 기념으로 학생들은 파티를 하고 있다. 엄지는 n(1≤n≤100,000)명의 학생에게 1부터 n번까지 차례대로 번호를 부여하였고 그들을 순서대로 빙 둘러앉아 원을 만들게 하였다. (즉 i번째 학생은 i-1과 i+1학생 사이에 앉아있다. 단, n번째 학생은 n-1번째 학생과 첫 번째 학생 사이에 앉아있다.)
# n명의 학생은 둘러앉아 "머리톡톡" 게임을 하려한다. 게임 규칙은 다음과 같다. 각각의 학생은 자신의 머리 위에 1,000,000 이하의 자연수 중 하나를 쓴다. 그리고 1번부터 n번 학생까지 한 명씩 차례대로 일어나 원을 돌면서 자신이 쓴 숫자가 다른 사람이 쓴 숫자의 배수이면 그 학생의 머리를 "톡톡" 친다.
# 문제는 각각의 학생이 일어나 자신의 자리로 돌아올 때까지 총 몇 명의 학생의 머리를 치는지 구하는 것이다.

import sys

input = sys.stdin.readline

n = int(input())
cir, ans = [], [0 for _ in range(n)]
for i in range(n):
    cir.append(int(input()))

matrix = [0 for _ in range(max(cir)+1)]
for num in cir:
    matrix[num] += 1

for i in range(n):
    k = 1
    while k*k <= (cir[i]):
        if cir[i] % k == 0:
            if k*k != cir[i]:
                ans[i] += matrix[k] + matrix[cir[i]//k]
            else:
                ans[i] += matrix[k]
        k += 1

for a in ans:
    print(a-1)