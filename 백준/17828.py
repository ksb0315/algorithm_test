# 작년에 소수나라에 다녀온 하나는, 올해는 문자열나라로 관광을 가려고 한다. 문자열나라에서는 특이하게 알파벳 대문자로 구성된 문자열을 화폐로 사용한다.
# 문자열나라에서 'A'는 1의 가치, 'B'는 2의 가치, ..., 'Z'는 26의 가치를 가지고 있으며, 이 알파벳들을 붙여 화폐로 쓰일 문자열을 만든다. 예를 들어, "HOnGIK"의 가치는 8 + 15 + 14 + 7 + 9 + 11 = 64가 된다.
# 소수나라에서 특이한 화폐 때문에 큰 스트레스를 받았던 하나는, 이번에는 정확한 소비 계획을 세워 미리 문자열 화폐로 돈을 환전해가려고 한다. 하나가 가져갈 문자열은 딱 하나이며, 길이는 n이고, 가치는 x여야 한다. 그리고 물론 알파벳 대문자로만 이루어져 있어야 한다.
# 그런데 환전소에서는 사전 순으로 앞서는 문자열을 우선적으로 환전해준다고 한다! 여행 준비에 정신이 없는 하나를 위해, 조건을 만족하면서 사전 순으로 가장 앞서는 문자열 구해주자.

n, x = map(int, input().split())

if n * 26 < x or n > x:
    print('!')
else:
    string_list = ['A'] * n
    x -= n
    i = n - 1

    while x > 0:
        if x >= 25:
            string_list[i] = 'Z'
            i -= 1
            x -= 25
        else:
            string_list[i] = chr(x + 65)
            break
    ans = ''
    for i in string_list:
        ans+=i
    # print(''.join(string_list))
    print(ans)