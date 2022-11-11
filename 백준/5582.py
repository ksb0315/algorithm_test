# 두 문자열이 주어졌을 때, 두 문자열에 모두 포함된 가장 긴 공통 부분 문자열을 찾는 프로그램을 작성하시오.
# 어떤 문자열 s의 부분 문자열 t란, s에 t가 연속으로 나타나는 것을 말한다. 예를 들어, 문자열 ABRACADABRA의 부분 문자열은 ABRA, RAC, D, ACADABRA, ABRACADABRA, 빈 문자열 등이다. 하지만, ABRC, RAA, BA, K는 부분 문자열이 아니다.
# 두 문자열 ABRACADABRA와 ECADADABRBCRDARA의 공통 부분 문자열은 CA, CADA, ADABR, 빈 문자열 등이 있다. 이 중에서 가장 긴 공통 부분 문자열은 ADABR이며, 길이는 5이다. 또, 두 문자열이 UPWJCIRUCAXIIRGL와 SBQNYBSBZDFNEV인 경우에는 가장 긴 공통 부분 문자열은 빈 문자열이다.

import sys
input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

x = len(str1)
y = len(str2)

dp = [[0] * (y+1) for _ in range(x+1)]

ans = 0
for i in range(1, x+1):
    for j in range(1, y+1):
        if str1[i-1] == str2[j-1]:
            dp[i][j] = dp[i-1][j-1]+1
            ans = max(ans, dp[i][j])
print(ans)