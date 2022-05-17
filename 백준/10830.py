#크기가 N*N인 행렬 A가 주어진다. 이때, A의 B제곱을 구하는 프로그램을 작성하시오. 수가 매우 커질 수 있으니, A^B의 각 원소를 1000으로 나눈 나머지를 출력한다.

n, b = map(int, input().split())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

def cum_mat(A, B):
    new_mat = [[0]* n for _ in range(n)]
    for row in range(n):
        for col in range(n):
            comp = 0
            for i in range(n):
                comp += A[row][i] * B[i][col]
            new_mat[row][col] = comp%1000
    return new_mat
    
def result(mat, k):
    if k == 1:
        for i in range(n):
            for j in range(n):
                mat[i][j] %= 1000
        return mat

    temp = result(mat, k//2)
    if k % 2 == 1:
        return cum_mat(cum_mat(temp, temp), mat)
    else:
        return cum_mat(temp, temp)

ans = result(matrix, b)
for a in ans:
    print(*a)
