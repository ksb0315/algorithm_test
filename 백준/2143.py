# 한 배열 sum_n_arr[1], sum_n_arr[2], …, sum_n_arr[n]에 대해서, 부 배열은 sum_n_arr[i], sum_n_arr[i+1], …, sum_n_arr[j-1], sum_n_arr[j] (단, 1 ≤ i ≤ j ≤ n)을 말한다. 이러한 부 배열의 합은 sum_n_arr[i]+…+sum_n_arr[j]를 의미한다. 각 원소가 정수인 두 배열 sum_n_arr[1], …, sum_n_arr[n]과 sum_m_arr[1], …, sum_m_arr[m]이 주어졌을 때, A의 부 배열의 합에 B의 부 배열의 합을 더해서 T가 되는 모든 부 배열 쌍의 개수를 구하는 프로그램을 작성하시오.
# 예를 들어 sum_n_arr = {1, 3, 1, 2}, sum_m_arr = {1, 3, 2}, t=5인 경우, 부 배열 쌍의 개수는 다음의 7가지 경우가 있다.
# t(=5) = sum_n_arr[1] + sum_m_arr[1] + sum_m_arr[2]
#       = sum_n_arr[1] + sum_n_arr[2] + sum_m_arr[1]
#       = sum_n_arr[2] + sum_m_arr[3]
#       = sum_n_arr[2] + sum_n_arr[3] + sum_m_arr[1]
#       = sum_n_arr[3] + sum_m_arr[1] + sum_m_arr[2]
#       = sum_n_arr[3] + sum_n_arr[4] + sum_m_arr[3]
#       = sum_n_arr[4] + sum_m_arr[2] 

import sys
import bisect

input = sys.stdin.readline
 
t = int(input()) 
n = int(input()) 
sum_n_arr = list(map(int,input().split())) 
m = int(input()) 
sum_m_arr = list(map(int,input().split())) 
 
result = 0
Asum = sum_n_arr
Bsum = sum_m_arr
for s in range(n):
    for e in range(s+1,n):
        Asum.append(sum(sum_n_arr[s:e+1])) 
for s in range(m):
    for e in range(s+1,m):
        Bsum.append(sum(sum_m_arr[s:e+1]))
 
Asum.sort()
Bsum.sort()
 
for i in range(len(Asum)):
    l = bisect.bisect_left(Bsum, t-Asum[i])
    r = bisect.bisect_right(Bsum, t-Asum[i])
    result+=r-l
print(result)