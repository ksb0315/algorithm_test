# 수직선과 같은 일직선상에 N개의 마을이 위치해 있다. i번째 마을은 X[i]에 위치해 있으며, A[i]명의 사람이 살고 있다.
# 이 마을들을 위해서 우체국을 하나 세우려고 하는데, 그 위치를 어느 곳으로 할지를 현재 고민 중이다. 
# 고민 끝에 나라에서는 각 사람들까지의 거리의 합이 최소가 되는 위치에 우체국을 세우기로 결정하였다. 우체국을 세울 위치를 구하는 프로그램을 작성하시오.
# 각 마을까지의 거리의 합이 아니라, 각 사람까지의 거리의 합임에 유의한다.

n = int(input())

array = []
for i in range(n):
    x,y = map(int, input().split())
    array.append([x,y])
    
array = sorted(array, key = lambda i : i[0])
pop = 0
for i in range(n):
    k = array[i][1] 
    pop = pop + k

mid = pop//2 

if (pop%2) != 0: 
    mid = mid + 1

pop_count = 0
for q,w in array:
    pop_count = pop_count + w 
    if pop_count >= mid:
        ans = q
        break
print(ans)
