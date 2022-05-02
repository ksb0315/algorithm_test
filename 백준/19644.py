# 킬로와 헥토는 좀비 떼로부터 탄약고를 사수하는 데에 성공했다. 포상 휴가나 조기 전역을 기대했으나 좀비 사태로 인해 계엄령이 선포되면서 오히려 전역이 연기되고 기관총 진지에 배치되었다.
# 전역이 연기된 킬로와 헥토에게 좀비 떼가 다가오기 시작했다.
# 기관총 진지 앞쪽 길의 거리는 L m이며, 진지로부터 i m 떨어진 곳에 있는 좀비의 체력은 Zi이다. 체력이 0 이하가 된 좀비는 영구적으로 죽는다.
# 기관총 진지에서 킬로와 헥토는 좀비가 1 m 이동할 때 기관총 또는 수평 세열 지향성 지뢰를 한 번 사용할 수 있다. 수평 세열 지향성 지뢰를 격발하는 경우 후폭풍을 피하기 위해 킬로와 헥토는 기관총 진지 밑으로 숨어야 한다. 즉, 수평 세열 지향성 지뢰 격발과 기관총 사격을 동시에 할 수는 없다.
# 기관총
# 유효 사거리는 진지 앞으로부터 ML m이다. 유효 사거리 내의 각 1 m 마다 좀비의 체력을 MK만큼 낮춘다. 
# 기관총 탄약은 엄청나게 많이 있으므로 신경쓰지 않아도 된다. 총열 교체나 장전, 총기 이상 등을 고려할 필요 없이 계속 사격할 수 있다고 가정한다.
# 수평 세열 지향성 지뢰
# 유효 사거리는 진지 앞으로부터 1 m이다. 하지만 진지 바로 앞 1 m의 좀비는 체력과 상관없이 제압할 수 있다.
# 수평 세열 지향성 지뢰는 Cammo개 있다. 
# 기관총 진지라곤 하나 콘크리트로 지어진 토치카가 아니라 사대로 구축한 임시 진지이기 때문에 1 m 떨어진 길 위의 좀비를 제압하지 못한다면 사망한다. 
# 과연 킬로와 헥토는 살아남을 수 있을까?

from sys import stdin
from collections import deque

l = int(stdin.readline()) 
ml, mk = map(int, stdin.readline().split()) 
c = int(stdin.readline()) 
zombie = [int(stdin.readline()) for i in range(l)] 

q = deque()

count = 0 
ans = True
for i in range(min(ml,l)): 
    if len(q)==0:
        if zombie[0]-mk <= 0:
            q.append(0)
        else:
            q.append(zombie[0])
            count+=1
    else:
        if count == 0:
            if zombie[i]-mk*(i+1) <= 0:
                q.append(0)
            else:
                q.append(zombie[i]-mk*(i+1))
                count+=1
        else:
            if zombie[i]-mk*(i+1-count) <= 0:
                q.append(0)
            else:
                q.append(zombie[i]-mk*(i+1-count))
                count+=1
        
for i in range(ml,l):
    if q[0] == 0:
        q.popleft()
        if zombie[i]-mk*(ml-count) <= 0:
            q.append(0)
        else:
            q.append(zombie[i]-mk*(ml-count))
            count+=1
    else:
        q.popleft()
        if c>0:
            c-=1
        else:
            ans = False
            break
        if zombie[i]-mk*(ml-count) <= 0:
            q.append(0)
            count-=1
        else:
            q.append(zombie[i]-mk*(ml-count))

if ans:
    while q:
        if q[0] == 0:
            q.popleft()
        else:
            q.popleft()
            count-=1
            if c>0:
                c-=1
            else:
                ans = False
                break

if ans:
    print("YES")
else:
    print("NO")