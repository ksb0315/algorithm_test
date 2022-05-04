# 음이 아닌 정수가 N개 들어있는 리스트가 주어졌을 때, 리스트에 포함된 수를 나열하여 만들 수 있는 가장 큰 수를 구하는 프로그램을 작성하시오.

n = int(input())
nums = list(map(int,input().split()))
greedy = []
for i in nums:
    s = str(i)
    leng = len(s)
    while len(s) < 10:
        s += s[len(s)-leng]
    greedy.append(([*list(s)],str(i)))
greedy.sort(key = lambda x : x[0], reverse = True)

ans = ""
for i in greedy:
    ans += i[-1]
print(ans if int(ans) != 0 else 0)