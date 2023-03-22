import sys

input = sys.stdin.readline

n, k = map(int, input().split())
ans = 0
lights = []
for _ in range(k):
    lights.append(list(map(int, input().split())))
lights.sort(key=lambda x: x[0])
for i in range(k):
    if i == 0:
        ans += lights[i][0] 
    else:
        ans += (lights[i][0] - lights[i-1][0])
    if (ans - lights[i][2]) < 0: # green
        ans += abs(ans - lights[i][2])
    elif ans - lights[i][2] > 0: # red or green
        if ((ans - lights[i][2]) // lights[i][1]) % 2 == 1: # red
            if (ans - lights[i][2]) % lights[i][1] == 0:
                ans += lights[i][1]
            else:
                temp = lights[i][2]
                while ans >= temp:
                    temp += lights[i][1]
                # ans += (ans - lights[i][2]) % lights[i][1]
                ans += temp % ans

ans += (n - lights[-1][0])

print(ans)