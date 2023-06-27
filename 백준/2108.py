# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()
print(round(sum(arr)/n))
print(arr[n//2])
set_arr = sorted(list(set(arr)))
dict_arr = {}
for i in range(len(arr)):
    if arr[i] not in dict_arr:
        dict_arr[arr[i]] = 0
    dict_arr[arr[i]] += 1
check_cnt = 0
temp = []
for k, v in dict_arr.items():
    if check_cnt < v:
        check_cnt = v
        temp = []
        temp.append(k)
    elif check_cnt == v:
        temp.append(k)
freq = 0
if len(temp) > 1:
    freq = temp[1]
else:
    freq = temp[0]
print(freq)
print(max(arr)-min(arr))