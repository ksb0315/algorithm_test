# 길이가 $n$인 수열 $arr$가 있다. 수열 $arr$는 1 이상인 정수로 이루어져 있다.수열 $arr$에서 원하는 위치에 있는 수를 골라 최대 $k$번 삭제를 할 수 있다. 예를 들어, 수열 $arr$가 다음과 같이 구성되어 있다고 가정하자.
# 수열 arr : 1 2 3 4 5 6 7 8
# 수열 $arr$에서 4번째에 있는 4를 지운다고 하면 아래와 같다.
# 수열 arr : 1 2 3 5 6 7 8 
# 수열 $arr$에서 최대 $k$번 원소를 삭제한 수열에서 짝수로 이루어져 있는 연속한 부분 수열 중 가장 긴 길이를 구해보자.

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = list(map(int, input().split()))

end = 0 
ans = 0 
temp = 0
cnt = 0 

for start in range(n):
    while (cnt <= k and end < n):             
        if arr[end] % 2 == 1:
            cnt += 1
        else:
            temp += 1
        end += 1 
        if start == 0 and end == n:
            ans = temp
            break
    
    if cnt == k+1 :
        ans = max(temp, ans)      
    if arr[start] %2 == 1:
        cnt -= 1
    else: 
        temp -= 1
        
print(ans)