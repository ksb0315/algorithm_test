# N(1 ≤ N ≤ 100)개의 수로 이루어진 1차원 배열이 있다. 이 배열에서 M(1 ≤ M ≤ ⌈(N/2)⌉)개의 구간을 선택해서, 구간에 속한 수들의 총 합이 최대가 되도록 하려 한다. 단, 다음의 조건들이 만족되어야 한다.
# 1. 각 구간은 한 개 이상의 연속된 수들로 이루어진다.
# 2. 서로 다른 두 구간끼리 겹쳐있거나 인접해 있어서는 안 된다.
# 3. 정확히 M개의 구간이 있어야 한다. M개 미만이어서는 안 된다.
# N개의 수들이 주어졌을 때, 답을 구하는 프로그램을 작성하시오.

n,m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
dp1 = [[-float('inf') for _ in range(m + 1)] for _ in range(n)]
dp2 = [[-float('inf') for _ in range(m + 1)] for _ in range(n)]
dp1[0][0] = 0
dp2[0][1] = arr[0]

for i in range(1, n):
    dp1[i][0] = 0
    dp2[i][0] = -float('inf')
    for j in range(1, min(m, (i + 2) // 2) + 1):
        dp1[i][j] = max(dp1[i-1][j], dp2[i-1][j])
        dp2[i][j] = max(dp1[i-1][j-1] + arr[i], dp2[i-1][j] + arr[i])


print(max(dp1[n-1][m], dp2[n-1][m]))


