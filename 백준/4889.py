# 여는 괄호와 닫는 괄호만으로 이루어진 문자열이 주어진다. 여기서 안정적인 문자열을 만들기 위한 최소 연산의 수를 구하려고 한다. 안정적인 문자열의 정의란 다음과 같다.
# 빈 문자열은 안정적이다.
# S가 안정적이라면, {S}도 안정적인 문자열이다.
# S와 T가 안정적이라면, ST(두 문자열의 연결)도 안정적이다.
# {}, {}{}, {{}{}}는 안정적인 문자열이지만, }{, {{}{, {}{는 안정적인 문자열이 아니다.
# 문자열에 행할 수 있는 연산은 여는 괄호를 닫는 괄호로 바꾸거나, 닫는 괄호를 여는 괄호로 바꾸는 것 2가지이다.

import sys

input = sys.stdin.readline

ans = []

while True:
    stack = []
    cnt = 0
    s = input().rstrip()
    if s.count('-') >= 1:
        break
    for i in range(len(s)):
        if not stack and s[i] == '}':
            cnt += 1
            stack.append('{')
        elif stack and s[i] == '}':
            stack.pop()
        else:
            stack.append(s[i])
    cnt += len(stack)//2
    ans.append(cnt)

for i in range(len(ans)):
    print(i+1, '. ', ans[i], sep='')