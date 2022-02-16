# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.
#     2를 곱한다.
#     1을 수의 가장 오른쪽에 추가한다. 
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.

s, e = map(int, input().split())
cnt = 1

while True:
    if s == e:
        break
    elif s > e or (e % 10 != 1 and e % 2 != 0):
        cnt = -1
        break
    elif e % 10 == 1:
        e //= 10
        cnt += 1
    elif e % 2 == 0:
        e //= 2
        cnt += 1
    
print(cnt)