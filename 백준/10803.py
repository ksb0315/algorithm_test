# 두 변의 길이가 모두 양의 정수인 직사각형 모양의 종이가 주어져 있다. 이 종이를 칼로 여러 번 잘라서 모든 조각이 한 변의 길이가 양의 정수인 정사각형이 되도록 하고자 한다. 
# 칼로 종이를 자르는 규칙은 다음과 같다.
# 1. 자르는 방향은 수직 또는 수평만 허용된다. 즉, 사선으로는 자를 수 없다.
# 2. 자르는 도중 칼의 방향을 바꿀 수 없다.
# 3. 자르는 도중에 칼을 멈출 수 없다. 즉, 일단 어떤 조각을 자르기 시작하면 그 조각이 반드시 둘로 분리될 때 까지 자른다.
# 4. 잘려진 조각의 각 변의 길이는 양의 정수이어야 한다. 
# 위의 규칙에 따라 주어진 직사각형 모양의 종이를 잘라 각 조각이 정사각형이 되도록 하되, 잘려진 조각 개수가 최소가 되도록 하고자 한다. 

width, height = map(int, input().split())
# dp = [[-1 for _ in range(10001)] for _ in range(101)]

def solve(n, m):
    global dp
    if n > m: return solve(m, n)
    if m % n ==0: return m//n

    # ans = dp[m][n]
    # if ans != -1: return ans
    ans = float('inf')
    q = m / n
    
    if q >= 3:
        ans = min(ans, solve(n, m - n) + 1)
    else:
        for i in range(1, (n//2)+1):
            ans = min(ans, solve(n - i, m) + solve(i, m))
        for i in range(1, (m//2)+1):
            ans = min(ans, solve(n, m-i) + solve(n, i))
    
    return ans


res = solve(min(width, height), max(width, height))
    
print(res)
#틀림
