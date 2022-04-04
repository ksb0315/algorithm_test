# 모든 값이 0으로 채워져 있는 길이가 N인 배열 A가 있다. 영선이는 다음과 같은 두 연산을 수행할 수 있다.
# 배열에 있는 값 하나를 1 증가시킨다.
# 배열에 있는 모든 값을 두 배 시킨다.
# 배열 B가 주어졌을 때, 배열 A를 B로 만들기 위한 연산의 최소 횟수를 구하는 프로그램을 작성하시오.

n = int(input())
obj_arr = list(map(int,input().split()))
cnt = 0
def find_even(arr):
    for i in arr:
        if i % 2 == 1:
            return False
    return True

def count_odd(arr):
    cnt = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 1:
            arr[i]-=1
            cnt+=1
    return cnt

while obj_arr.count(0) != len(obj_arr):
    flag = find_even(obj_arr)
    if flag == True:
        for i in range(n):
            obj_arr[i] = obj_arr[i]//2
        cnt+=1
    elif flag == False:
        cnt += count_odd(obj_arr)
print(cnt)