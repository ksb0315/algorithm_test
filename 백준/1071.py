# n개의 정수가 주어지면, 이것을 연속된 두 수가 연속된 값이 아니게 정렬(A[i] + 1 ≠ A[i+1])하는 프로그램을 작성하시오. 가능한 것이 여러 가지라면 사전순으로 가장 앞서는 것을 출력한다.

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
 
num_cnt = [0]*1005
 
for num in arr:
    num_cnt[num] += 1

cur = 0
result = []
while sum(num_cnt)>0:
    if num_cnt[cur]:
        if num_cnt[cur+1]:
            for next_num in range(cur+2,1001):
                if num_cnt[next_num]:
                    result.extend(num_cnt[cur]*[cur])
                    result.append(next_num)
                    num_cnt[cur] = 0
                    num_cnt[next_num] -= 1
                    break
            else:
                result.extend(num_cnt[cur+1]*[cur+1])
                result.extend(num_cnt[cur]*[cur])
                num_cnt[cur] = 0
                num_cnt[cur+1] = 0
 
        else:
            while num_cnt[cur]:
                result.append(cur)
                num_cnt[cur] -= 1
    cur += 1

for res in result:
    print(res, end=' ')