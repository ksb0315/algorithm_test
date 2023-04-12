# 아우으 우아으이야!! 으어아아아아아아아ㅏㅏㅏ아아앙ㅇ아아ㅏ
# 수직선 위에 선분을 여러 개 그릴 거 야아아앙ㅇ아아아ㅏㅏ아아ㅏㅏ!!
# 선분을 겹치게 그리는 것도 가능하다아어으우어우으아아아아아아아아아이야!!!!1
# 선분을 모두 그렸을 때, 수직선 위에 그려진 선분 길이의 총합은 얼마아아으으우어으이으야이야!!!!

import sys

input = sys.stdin.readline

n = int(input())

sum_len = 0
start, end = map(int, input().split())
    
for _ in range(n-1):
    a, b = map(int, input().split())
    if a <= end:
        if b >= end: # case2
            end = b
    else: # case3
        sum_len += (end - start)
        start = a
        end = b

print(sum_len + (end - start))