# 인기 펑크 락밴드 SHOM은 새 앨범을 내기로 했다. SHOM의 새 앨범에는 총 N개의 노래가 들어간다. SHOM은 요번 앨범에는 새로운 시도를 했는데, 앨범에 수록되는 모든 노래의 길이가 모두 같다.
# 시디 한 장에는 C초만큼의 노래를 저장할 수 있다.
# 숌은 N개의 곡을 모두 앨범에 넣고 싶은 욕망이 있었기 때문에, N개의 곡을 몇 장의 씨디로 나누어야 할지 궁금해졌다. 하지만, 가격을 위해 시디의 개수를 최소화하고 싶었다.
# 하지만, SHOM의 보컬 이다솜은 자신의 미신 때문에, 절대로 시디에 녹음되는 노래의 개수가 13으로 나누어 떨어지면 안 된다는 조건을 걸었다.
# 시디에 노래를 두 곡이상 수록할 때, 어떤 노래와 어떤 노래 사이에는 1초의 공백이 반드시 필요하다.
# SHOM의 새 앨범은 총 몇 장으로 발매될지 구하는 프로그램을 작성하시오.

import sys

input=sys.stdin.readline

n = int(input())
leng = int(input())
cd_leng = int(input())

a = cd_leng // (leng+1)
k = cd_leng % (leng+1)

if k == leng:
    a += 1
a = min(n, a)
if a % 13 == 0:
    a-=1

ans = n // a
x = n % a
k = a
if x != 0:
    ans += 1
    if x % 13 == 0:
        while not (k % 13 and x % 13):
            k -= 1
            x += 1
        ans += x // a

print(ans)