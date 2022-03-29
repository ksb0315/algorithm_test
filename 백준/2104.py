# 크기가 N(1 ≤ N ≤ 100,000)인 1차원 배열 A[1], …, A[N]이 있다. 어떤 i, j(1 ≤ i ≤ j ≤ N)에 대한 점수는, (A[i] + … + A[j]) × min{A[i], …, A[j]}가 된다. 즉, i부터 j까지의 합에 i부터 j까지의 최솟값을 곱한 것이 점수가 된다.
# 배열이 주어졌을 때, 최대의 점수를 갖는 부분배열을 골라내는 프로그램을 작성하시오.
def solve(s, e):
    if s == e:
        return A[s] * A[s]
    mid = (s+e)//2
    ret = max(solve(s, mid), solve(mid+1, e))

    left = mid
    right = mid + 1
    _sum = A[left] + A[right]
    min_val = min(A[left], A[right])
    ret = max(ret, min_val * _sum)
    while left > s or right < e:
        if right < e and (left == s or A[left-1] < A[right + 1]):
            right += 1
            _sum += A[right]
            min_val = min(min_val, A[right])
        else:
            left -= 1
            _sum += A[left]
            min_val = min(min_val, A[left])
        ret = max(ret, min_val * _sum)
    return ret

input()
A = list(map(int, input().split()))
print(solve(0, len(A)-1))