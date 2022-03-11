# 피자를 굽는 전자식 오븐이 있다. 이 오븐에 재료는 넣고 정확히 $N$분 동안 동작을 시키고자 한다. 그런데 이 오븐에 준비된 버튼은 아래와 같은 동작을 하는 5가지이다. 
# 즉, 각각의 버튼은 동작 시간을 추가시키거나 감소시킨다. 처음에 피자 오븐의 첫 시간은 0분으로 정해져 있다. 시간을 감소시키는 버튼을 눌러서 시간이 0분보다 작아지는 경우에는 0분으로 설정된다. $t$가 현재 오븐에 세팅된 시간, $t'$은 버튼을 누른 뒤의 시간을 의미할 때, 각 버튼은 다음과 같은 기능을 가지고 있다.
# ADDH: t' = t + 60$
# ADDT: t' = t + 10$
# MINT: t' = t - 10$
# ADDO: t' = t + 1$
# MINO: t' = t - 1$
# 예를 들어, 58분을 설정하고 싶으면, ADDO (+1분) 버튼을 58번 눌러도 된다. 하지만, ADDH (+60분) 버튼을 한 번 누른 뒤에 MINO (-1분) 버튼을 2번 누르면 3번의 작업으로 58분을 만들 수 있다. 42분을 설정하고 싶은 경우에는 버튼을 ADDH, MINT, MINT, ADDO, ADDO 순서로 5번 눌러서 만들 수 있다. ADDT, ADDT, ADDT, ADDT, ADDO, ADDO 순서로 6번 눌러서 만들 수 있지만, 버튼은 최소 횟수로 누르려고 한다.
# 설정해야 할 시간이 주어졌을 때, 그 시간을 만들기 위해 눌러야 하는 버튼의 최소 횟수와 그 방법을 구하는 프로그램을 작성하시오.

case = int(input())
ans = []
for _ in range(case):
    n = int(input())
    buttons = [0]*5
    sixties, tens, ones = n//60, (n % 60)//10, n % 10

    if ones > 5:
        tens += 1
        ones -= 10
    if tens > 3:
        sixties += 1
        tens -= 6
    if tens < 0 and ones == 5:
        tens += 1
        ones -= 10

    buttons[0] = sixties
    buttons[2-(tens >= 0)] = abs(tens)
    buttons[4-(ones >= 0)] = abs(ones)
    ans.append(buttons)
    
for i in ans:
    for j in i:
        print(j, end=' ')
    print()