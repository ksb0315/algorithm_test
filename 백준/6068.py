# 성실한 농부 존은 시간을 효율적으로 관리해야 한다는 걸 깨달았다. 그는 N개의 해야할 일에 (1<=N<=1000) 숫자를 매겼다. (우유를 짜고, 마굿간을 치우고, 담장을 고치는 등의)
# 존의 시간을 효율적으로 관리하기 위해, 그는 끝내야만 하는 일 목록을 만들었다. 완성될 때 필요한 시간을 T_i(1<=T_i<=1,000) 라고 하며, 끝내야하는 시간을 S_i(1<=S_i<=1,000,000) 이라 한다. 농부 존은 하루의 시작을 t = 0으로 정했다. 그리고 일 할 때는 그 일을 마칠 때 까지 그 일만 한다. 
# 존은 늦잠 자는 걸 좋아한다. 따라서 제 시간에 끝낼 수 있게 결정할 수 있는 한도에서 존이 가장 늦게 일어나도 되는 시간을 출력하라.

import sys

input = sys.stdin.readline
n = int(input())
time = []
for _ in range(n):
    time.append(list(map(int,input().split())))

time.sort(key=lambda x : x[1], reverse=True)

done = time[0][1]-time[0][0]
for i in range(1, n):
    if done < time[i][1]:
        time[i][1]=done
    done = time[i][1]-time[i][0]
if done < 0:
    print(-1)
else:   
    print(done)
