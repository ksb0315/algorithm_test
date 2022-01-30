# 임한수와 임문빈은 서로 사랑하는 사이이다.
# 임한수는 세상에서 팰린드롬인 문자열을 너무 좋아하기 때문에, 둘의 백일을 기념해서 임문빈은 팰린드롬을 선물해주려고 한다.
# 임문빈은 임한수의 영어 이름으로 팰린드롬을 만들려고 하는데, 임한수의 영어 이름의 알파벳 순서를 적절히 바꿔서 팰린드롬을 만들려고 한다.
# 임문빈을 도와 임한수의 영어 이름을 팰린드롬으로 바꾸는 프로그램을 작성하시오.

name = input()
name_list = list(name)
name_list.sort(reverse=True) # [C, B, B, A, A, A, A]
name_set = set(name_list)
alpa = list(name_set)
cnt = 0
alpa.sort() # [A, B, C]
count = [] #[4, 2, 1]
ans = ''

for a in alpa:
    count.append(name.count(a))
    if name.count(a) % 2 == 1:
        cnt += 1
    if cnt > 1:
            print("I'm Sorry Hansoo")
            exit(0)

for i in range(len(count)):
    for _ in range(count[i]-1):
        name_list.pop()
    ans += name_list.pop() * (count[i]//2)

for i in range(len(count)):
    if count[i] % 2 == 0:
        count[i] = count[i]//2
    else:
        ans += alpa[i]
        count[i] = count[i]//2

for i in range(len(count)):
    for _ in range(count[i]):
        name_list.append(alpa[i])

for _ in range(len(name_list)):
    ans += name_list.pop()

print(ans)