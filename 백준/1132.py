# N개의 수가 주어진다. 이 숫자는 모두 자연수이고, 알파벳 A부터 J가 자리수를 대신해서 쓰여 있다. 이 알파벳은 모두 한 자리를 의미한다. 그리고, 각 자리수는 정확하게 알파벳 하나이다. 0으로 시작하는 수는 없다. 이때, 가능한 수의 합 중 최댓값을 구해보자.

n = int(input())
a = [[0, False] for _ in range(10)]
ans = 0
for _ in range(n):
    s = input()
    m = 1
    a[ord(s[0])-65][1] = True
    for c in range(len(s)-1, -1, -1):
        a[ord(s[c])-65][0] += m
        m *= 10

a.sort(reverse=True)
if a[9][1]:
    for i in range(8, -1, -1):
        if not a[i][1]:
            del a[i]
            break
for i in range(9):
    ans += a[i][0] * (9-i)

print(ans)