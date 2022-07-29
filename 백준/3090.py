# 정수 N개로 이루어진 배열 A가 주어진다. 상근이는 수열의 수 하나를 골라서 값을 1 감소시킬 수 있다. 단, 수는 1보다 작아질 수 없다.
# 상근이는 위의 감소시키는 연산을 최대 T번 하려고 한다. 이때, 인접한 수의 차이의 최댓값을 최소로 하는 프로그램을 출력하시오.

import sys, copy

input = sys.stdin.readline
 
N, T = map(int, input().split())
arr = list(map(int, input().split()))
 
 
def investigate(gap):
    global tempArr
    tempArr = copy.deepcopy(arr)
    operCount = 0
 
    for i in range(N - 1):
        if tempArr[i + 1] - tempArr[i] > gap:
            operCount += tempArr[i + 1] - (tempArr[i] + gap)
            tempArr[i + 1] = tempArr[i] + gap
    
    for i in range(N - 1, 0, -1):
        if tempArr[i - 1] - tempArr[i] > gap:
            operCount += tempArr[i - 1] - (tempArr[i] + gap)
            tempArr[i - 1] = tempArr[i] + gap
    
    if operCount <= T:
        return True
    return False
 
 
left = 0
right = 1000000000
result = []
 
while left <= right:
    mid = (left + right) // 2
 
    if investigate(mid):
        result = copy.deepcopy(tempArr)
        right = mid - 1
    else:
        left = mid + 1
 
print(*result)
