# 크기가 N인 배열 A가 있다. 배열에 있는 모든 수는 서로 다르다. 이 배열을 소트할 때, 연속된 두 개의 원소만 교환할 수 있다. 그리고, 교환은 많아봐야 S번 할 수 있다. 이때, 소트한 결과가 사전순으로 가장 뒷서는 것을 출력한다.

n=int(input())
arr = list(map(int, input().split()))
c=int(input())

for i in range(len(arr)):
	j=len(arr)
	while True:
		if i == arr.index(max(arr[i:j])):
			break
		else:
			if arr.index(max(arr[i:j]))-i <= c:
				max_idx = arr.index(max(arr[i:j]))
				c-= max_idx-i
				for k in range(max_idx-1,i-1,-1):
					arr[k],arr[k+1] = arr[k+1],arr[k]
			else:
				j-=1
print(' '.join(map(str, arr)))