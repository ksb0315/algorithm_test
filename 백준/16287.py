# 국제대학소포센터(ICPC: International Collegiate Parcel Center)는 전세계 대학생들을 대상으로 소포 무료 배송 이벤트를 진행하고 있다. 
# 무료 배송 조건은 보낼 소포가 물품 4개로 구성되어야 하며 이들 물품의 무게 합이 정확히 정해진 정수 무게 w 그램이어야 한다는 것이다.
# 부산대학교에 있는 찬수는 영국 왕립대학에 있는 수환에게 보낼 물품이 매우 많이 있는데, 각 물품의 무게(모두 정수 그램)는 모두 다르다.
#  이 이벤트는 한시적으로 진행되는 이벤트이기 때문에 찬수는 자신이 보낼 물품 중에서 이 조건을 만족하는 물품 4개가 있는지 가능하면 빨리 알아내고 싶다. 
# 다시 말해서 서로 다른 n(n ≥ 4)개의 정수로 이루어진 집합 A에서 4개의 원소만 꺼내어 만든 부분집합 B(|B| = 4)가 ∑b∈B b = w 조건을 만족하는지 판단하려고 한다. 
# 주어진 w와 A에 대해서, 위 조건을 만족하는 부분집합 B가 존재하면 YES를, 아니면 NO를 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

w, n = map(int, input().split())
parcel = list(map(int, input().split()))
memo = [False] * w

for i in range(n):
    for j in range(i+1,n):
        if parcel[i] + parcel[j] < w and memo[w - parcel[i] - parcel[j]]:
            print("YES")
            sys.exit(0)
    for j in range(i):
        if parcel[i] + parcel[j] < w:
            memo[parcel[i] - parcel[j]] = True

print("NO")

import sys
input = sys.stdin.readline
 
w, n = map(int, input().split())
A = list(map(int, input().split()))
memoization = [False] * w
 
for i in range(n):
    for j in range(i + 1, n):
        if A[i] + A[j] < w and memoization[w - A[i] - A[j]]:
            print("YES")
            sys.exit(0)
    
    for j in range(i):
        if A[i] + A[j] < w:
            memoization[A[i] + A[j]] = True
 
print("NO")