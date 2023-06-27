# 다항식(polynomial)은 문자의 거듭제곱의 상수 배들의 합을 표현하는 수식이다. 
# 예를 들어 x2+2x+3 같은 식을 의미한다. 그중 변수가 하나인 것을 일변수 다항식이라고 하고 이는 다음과 같이 표현한다.
# f(x) = axn + bxn-1+...+cx+d
# 최대 일차 일변수 다항식이 주어졌을 때 그 함수를 적분한 결과를 출력하는 프로그램을 작성하시오.

import sys
import collections

input = sys.stdin.readline
 
eq = input()
 
def integrate(term):
    t_dic = collections.Counter(term)
    a=term[:len(term)-t_dic["x"]]
    a = int(a) if len(a) != 0 else 1
    
    b = str(a//(t_dic["x"]+1))
    result = b + "x" * (t_dic["x"]+1) if b != "1" else "x" * (t_dic["x"]+1)
    return result
 
op = ["+","-"]
if eq[0] in op:
    answer = eq[0]
    start = 1
    end = 1
else :
    answer = ""
    start = 0
    end = 0
if eq[start] == "0":
    print("W")
else:
    while end < len(eq):
        if eq[end] not in op:
            end += 1
        else:
            answer += integrate(eq[start:end])
            #부호
            answer += eq[end]
            start = end + 1
            end += 1
    answer += integrate(eq[start:])+"+W"
    print(answer)
