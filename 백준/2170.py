# 매우 큰 도화지에 자를 대고 선을 그으려고 한다. 선을 그을 때에는 자의 한 점에서 다른 한 점까지 긋게 된다. 선을 그을 때에는 이미 선이 있는 위치에 겹쳐서 그릴 수도 있는데, 여러 번 그은 곳과 한 번 그은 곳의 차이를 구별할 수 없다고 하자.
# 이와 같은 식으로 선을 그었을 때, 그려진 선(들)의 총 길이를 구하는 프로그램을 작성하시오. 선이 여러 번 그려진 곳은 한 번씩만 계산한다.
import sys
input = sys.stdin.readline
n = int(input()) 
origin_lines = list(tuple(map(int, input().split())) for _ in range(n)) 
origin_lines.sort() 
start = origin_lines[0][0] 
end = origin_lines[0][1] 
ans = 0 
for k in range(1, n): 
    now_start, now_end = origin_lines[k] 
    if end > now_start: 
        end = max(end, now_end)
    else:
        ans += (end - start)
        start, end = now_start, now_end 

ans += (end - start) 
print(ans)
