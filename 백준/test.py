# 1. 상자 이동
#     - 입력
#         - x : 시작 위치
#         - y : 도착 위치
#         - z : 최대 이동 회수
#     - 문제
#         일렬로 나열된 상자가 있다. 최대 z번 이동가능하고, x에서 y로 이동해야한다.
#         최대 이동가능 횟수 내에 이동을 할 수 있을 때 최대 도달가능 인덱스 상자는 얼마인가?
#         만약 y에 도착하지 못하면 -1을 출력하라
# time complexity : O(1)

def solution1(x, y, z):
    r = z - abs(x - y)
    if r < 0:
        return -1
    else:
        if r % 2 == 0: # 남은 r이 짝수면 (가장 먼) 마지막 인덱스까지 도달했다가 도착 인덱스까지 도착 가능
            return max(y + r//2, x, y)
        else: # 남은 r이 홀수면 (가장 먼) 마지막 인덱스까지 도달했다가 도착 인덱스까지 도착 불가능
            return -1

print(solution1(3, 0, 5))


# 2. 색깔 구매
#     - 입력
#         - cost = [10,20,30] > 각 색깔마다의 가격
#         - x = 가진 자산
#     - 문제      
#         색깔을 구매를 하려고 한다. cost의 i 인덱스를 구매를 하려고 하면 cost[i]의 가격으로 2^i 개를 살 수 있다.
#         가진 자산 내에서 가장 많이 구매를 할 수 있는 방법으로 구매를 했을 때 몇 개의 색연필을 구매할 수 있는가?
#         (10^9 + 7) 보다 커지면 해당 값으로 모듈러 연산을 수행
# time complexity : O(N)

def solution2(cost, x):
    res = 0
    cost = list(reversed(cost))
    for i in range(len(cost)):
        if x >= cost[i]:
            x -= cost[i]
            res += 2 ** i
    return (res % (10 ** 9 + 7))

print(solution2([10, 20, 30], 50))

# - 3. 빵 옮기기
#     - 입력
#         - box = [10,3,5,31]
#     - 문제        
#         각 상자마다 빵이 담겨져 있고 그 개수를 box에 기록해둔다.        
#         빵을 뒤에서 앞으로만 옮길 수 있다.
#         옮기는 과정이 모두 끝나고 가장 많은 개수를 가진 박스의 빵의 개수가 최소가 되도록 해야한다.        
#         옮기는 과정이 끝나고 최대 빵의 개수는 얼마인가?   
# time complexity : O(N)     

def solution3(box):
    # ‘가장 많은 개수를 가진 박스의 빵의 개수가 최소가 되도록’하려면 mean에 가깝게 빵을 옮겨야한다.
	cal = []
	s = 0

	# (i+1)번째 box까지 각 box에 들어가야할 빵의 개수 (각 box에 mean 만큼 들어가야함)
	for i in range(len(box)):
		s += box[i]
		cal.append(s / (i + 1))

    # m =  box에 들어가야할 빵의 평균값 중 가장 큰 값
    # 현재 가장 많은 빵이 들어있는 box의 개수를 줄이기 위해
	m = max(cal)
    
	if m - int(m) > 0: # 소수점이 있는경우 각 box안의 빵은 m개 또는 m+1개 이므로 이 중 가장 큰 값이 필요하기 때문에
		return int(m) + 1
	else:
		return int(m) # 소수점이 없는경우 각 box안의 빵 중 가장 큰 값은 m 이다


print(solution3([10, 3, 5, 31]))