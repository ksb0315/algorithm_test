# 1부터 N까지의 수를 이어서 쓰면 다음과 같이 새로운 하나의 수를 얻을 수 있다.
# 1234567891011121314151617181920212223...
# 이렇게 만들어진 새로운 수에서, 앞에서 k번째 자리 숫자가 어떤 숫자인지 구하는 프로그램을 작성하시오.

n, k = map(int, input().split())
ans = 0
digit = 1
nine = 9

while k > digit*nine:
    k = k-(digit * nine)
    ans = ans + nine
    digit+=1
    nine = nine*10

ans = (ans+1) + (k-1) // digit

if ans > n:
    print(-1)
else:
    print(str(ans)[(k-1)%digit])