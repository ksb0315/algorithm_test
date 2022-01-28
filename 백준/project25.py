# 0과 1로만 이루어진 행렬 A와 행렬 B가 있다. 이때, 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하는 프로그램을 작성하시오
# 행렬을 변환하는 연산은 어떤 3×3크기의 부분 행렬에 있는 모든 원소를 뒤집는 것이다. (0 → 1, 1 → 0)

n, m = map(int, input().split())
matrix1 = []
matrix2 = []
count = 0

def convertgraph(i, j):			# 3x3을 뒤집는 함수
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            matrix1[x][y] = 1 - matrix1[x][y]

for i in range(n):				# 변환 전 함수 입력
    matrix1.append(list(map(int, input())))

for i in range(n):				# 변환 후 함수 입력
    matrix2.append(list(map(int, input())))

for i in range(n-2):
    for j in range(m-2):
        if matrix1[i][j] != matrix2[i][j]: # 일치하지 않은 요소
            convertgraph(i,j)
            count += 1

for i in range(n):
    for j in range(m):
        if matrix1[i][j] != matrix2[i][j]:
            count = -1
            break

print(count)
        
