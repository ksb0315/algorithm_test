import heapq

n = int(input())
arr = []
ans = []
for _ in range(n):
    num = int(input())
    if num < 0:
        heapq.heappush(arr, (-num,-1))
    elif num > 0:
        heapq.heappush(arr, (num, 1))
    else:
        if arr:
            a, b = heapq.heappop(arr)
            if b == -1:
                ans.append(-a)
            else:
                ans.append(a)
        else:
            ans.append(0)

for a in ans:
    print(a)