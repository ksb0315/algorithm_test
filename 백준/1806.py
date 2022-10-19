# 10,000 이하의 자연수로 이루어진 길이 N짜리 수열이 주어진다. 이 수열에서 연속된 수들의 부분합 중에 그 합이 S 이상이 되는 것 중, 가장 짧은 것의 길이를 구하는 프로그램을 작성하시오

import sys

input = sys.stdin.readline

n, s = map(int, input().split())
arr = list(map(int,input().split()))

start = 0 
end = 0
temp_sum = 0
ans = sys.maxsize

while True:
    if temp_sum >= s:
        ans = min(ans, end - start)
        temp_sum -= arr[start]
        start += 1
    elif end == n: break
    else:
        temp_sum += arr[end]
        end += 1        
        
if ans == sys.maxsize:
    print(0)
else:
    print(ans)