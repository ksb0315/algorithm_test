# 대부분의 양의 정수는 적어도 2개 이상의 연속된 자연수의 합으로 나타낼 수 있다.
# 예를 들면 다음과 같다.
# 6 = 1 + 2 + 3
# 9 = 5 + 4 = 4 + 3 + 2
# 하지만, 8은 연속된 자연수 합으로 나타낼 수가 없다.
# 자연수 N이 주어졌을 때, 이 수를 적어도 2개 이상의 연속된 자연수의 합으로 나타낼 수 있는 경우의 수를 출력하시오.

case = int(input())
ans = []
for _ in range(case):
    n = int(input())
    cnt = 0
    n-=1
    for i in range(2,n+1):
        n-=i
        cnt += 1 if n % i == 0 else 0	
        if n <= 0:
            break
    ans.append(cnt)

for i in ans:
    print(i)