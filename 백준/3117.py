# 1부터 N까지의 수를 한 번씩 이용해서 가장 긴 증가하는 부분 수열의 길이가 M이고, 가장 긴 감소하는 부분 수열의 길이가 K인 수열을 출력한다.

n = int(input())

arr = list(map(int, input().split()))
dp = [0] * n

for i in range(n):
    for j in range(i):
         if arr[i] > arr[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))

n = int(input())
des = list(map(int, input().split()))

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if des[j] > des[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))