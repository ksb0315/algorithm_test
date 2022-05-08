# 수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 프로그램을 작성하시오
# 예를 들어, 수열 A = {10, 20, 10, 30, 20, 50} 인 경우에 가장 긴 증가하는 부분 수열은 A = {10, 20, 10, 30, 20, 50} 이고, 길이는 4이다.

n = int(input()) 
cases = list(map(int, input().split())) 
lis = [0] 
for case in cases: 
    if lis[-1]<case: 
        lis.append(case) 
    else: 
        left = 0 
        right = len(lis) 
        while left<right: 
            mid = (right+left)//2 
            if lis[mid]<case: 
                left = mid+1 
            else: 
                right = mid 
        lis[right] = case 

print(len(lis)-1)
 