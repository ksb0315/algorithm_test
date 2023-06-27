# 홍대병에 걸린 도현이는 겹치는 것을 매우 싫어한다. 특히 수열에서 같은 원소가 여러 개 들어 있는 수열을 싫어한다. 도현이를 위해 같은 원소가 $k$개 이하로 들어 있는 최장 연속 부분 수열의 길이를 구하려고 한다.
# $100\,000$ 이하의 양의 정수로 이루어진 길이가 $n$인 수열이 주어진다.  이 수열에서 같은 정수를 $k$개 이하로 포함한 최장 연속 부분 수열의 길이를 구하는 프로그램을 작성해보자.

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 0, 0

cnt = [0] * (max(arr) + 1)
ans = 0
while e < n:
    if cnt[arr[e]] < k:
        cnt[arr[e]] += 1
        e += 1
    else:
        cnt[arr[s]] -= 1
        s += 1
    ans = max(ans, e - s)
print(ans)