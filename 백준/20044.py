# bryan은 PPAP를 좋아한다. bryan은 어떻게 하면 사람들에게 PPAP를 전파할 수 있을까 고민하던 중 PPAP 문자열이라는 것을 고안하게 되었다.
# PPAP 문자열은 문자열 P에서 시작하여, 문자열 내의 P를 PPAP로 바꾸는 과정을 반복하여 만들 수 있는 문자열로 정의된다. 정확하게는 다음과 같이 정의된다.
#   P는 PPAP 문자열이다.
#   PPAP 문자열에서 P 하나를 PPAP로 바꾼 문자열은 PPAP 문자열이다.
# 예를 들어 PPAP는 PPAP 문자열이다. 또한, PPAP의 두 번째 P를 PPAP로 바꾼 PPPAPAP 역시 PPAP 문자열이다.

p = input()

if p == 'PPAP' or p == 'P':
    print('PPAP')
else:
    stack = []
    ppap = ['P','P','A','P']
    for i in p:
        stack.append(i)
        if stack[-4:] == ppap:
            stack.pop()
            stack.pop()
            stack.pop()
    if stack == ppap or stack ==['P']:
        print('PPAP')
    else:
        print('NP')