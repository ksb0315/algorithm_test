# 기숙사에서 살고 있는 준규는 한 개의 멀티탭을 이용하고 있다. 준규는 키보드, 헤어드라이기, 핸드폰 충전기, 디지털 카메라 충전기 등 여러 개의 전기용품을 사용하면서 어쩔 수 없이 각종 전기용품의 플러그를 뺐다 꽂았다 하는 불편함을 겪고 있다. 그래서 준규는 자신의 생활 패턴을 분석하여, 자기가 사용하고 있는 전기용품의 사용순서를 알아내었고, 이를 기반으로 플러그를 빼는 횟수를 최소화하는 방법을 고안하여 보다 쾌적한 생활환경을 만들려고 한다.
# 예를 들어 3 구(구멍이 세 개 달린) 멀티탭을 쓸 때, 전기용품의 사용 순서가 아래와 같이 주어진다면, 

# 1. 키보드
# 2. 헤어드라이기
# 3. 핸드폰 충전기
# 4. 디지털 카메라 충전기
# 5. 키보드
# 6. 헤어드라이기

# 키보드, 헤어드라이기, 핸드폰 충전기의 플러그를 순서대로 멀티탭에 꽂은 다음 디지털 카메라 충전기 플러그를 꽂기 전에 핸드폰충전기 플러그를 빼는 것이 최적일 것이므로 플러그는 한 번만 빼면 된다. 
import sys
input = sys.stdin.readline

N, K = map(int, input().split())

multitap = list(map(int, input().split()))

plugs = []
count = 0

for i in range(K):
    # 있으면 건너 뛴다.
    if multitap[i] in plugs:
        continue
  
    # 플러그가 1개라도 비어 있으면 집어넣는다.
    if len(plugs) < N:
        plugs.append(multitap[i])
        continue
  
    multitap_idxs = [] # 다음 멀티탭의 값을 저장.
    hasplug = True

    for j in range(N):
  	    # 멀티탭 안에 플러그 값이 있다면
        if plugs[j] in multitap[i:]:
            # 멀티탭 인덱스 위치 값 가져오기.
            multitap_idx = multitap[i:].index(plugs[j])
        else:
            multitap_idx = 101
            hasplug = False

        # 인덱스에 값을 넣어준다.
        multitap_idxs.append(multitap_idx)
    
        # 없다면 종료
        if not hasplug:
            break
  
    # 플러그를 뽑는다.
    plug_out = multitap_idxs.index(max(multitap_idxs))
    del plugs[plug_out] # 플러그에서 제거
    plugs.append(multitap[i]) # 플러그에 멀티탭 값 삽입
    count += 1 # 뽑았으므로 1 증가

print(count)