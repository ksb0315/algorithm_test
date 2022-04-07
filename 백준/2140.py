# 지뢰찾기는 n×n에서 이뤄지는 게임이다. 보드의 곳곳에는 몇 개의 지뢰가 숨겨져 있고, 지뢰가 없는 칸에는 그 칸과 인접(상하좌우 및 대각선)해 있는 8개의 칸들에 몇 개의 지뢰가 숨겨져 있는지에 대한 정보가 주어진다. 
# 게이머는 게임을 진행하면서 보드의 칸을 하나씩 열게 된다. 만약 그 칸에 지뢰가 있다면 게임이 끝나고, 없는 경우에는 그 칸에 적혀있는 숫자, 즉 그 칸과 인접해 있는 8개의 칸들 중 몇 개의 칸에 지뢰가 있는지를 알 수 있게 된다.
# 이 문제는 보드의 테두리가 모두 열려있고, 그 외는 모두 닫혀있는 상태에서 시작한다.
# #는 닫혀있는 칸을 나타낸다. 이러한 보드가 주어졌을 때, 닫혀있는 칸들 중 최대 몇 개의 칸에 지뢰가 묻혀있는지 알아내는 프로그램을 작성하시오. 위의 예와 같은 경우에는 다음과 같이 6개의 지뢰가 묻혀있을 수 있다.

n = int(input())
mine =[]
for _ in range(n):
    temp = list(input())
    mine.append(temp)
cnt = 0
def search (arr,i,j):
    global n
    flag = 0
    if arr[i-1][j-1] == '0' or arr[i-1][j] == '0' or arr[i-1][j+1] == '0' or arr[i][j-1] == '0' or arr[i][j+1] == '0' or arr[i+1][j-1]=='0' or arr[i+1][j] == '0' or arr[i+1][j+1] == '0':
        flag = 0
    else:
        if arr[i-1][j-1] != '#':
            arr[i-1][j-1]=str(int(arr[i-1][j-1])-1)
        if arr[i-1][j] != '#':
            arr[i-1][j]=str(int(arr[i-1][j])-1)
        if arr[i-1][j+1] != '#':
            arr[i-1][j+1]=str(int(arr[i-1][j+1])-1)
        if arr[i][j-1] != '#':
            arr[i][j-1]=str(int(arr[i][j-1])-1)
        if arr[i][j+1] != '#':    
            arr[i][j+1]=str(int(arr[i][j+1])-1)
        if arr[i+1][j-1] != '#':
            arr[i+1][j-1]=str(int(arr[i+1][j-1])-1)
        if arr[i+1][j] != '#':
            arr[i+1][j]=str(int(arr[i+1][j])-1)
        if arr[i+1][j+1] != '#':
            arr[i+1][j+1]=str(int(arr[i+1][j+1])-1)
        flag = 1
        
    return flag

for i in range(1, n-1):
        for j in range(1, n-1):
            cnt += search(mine, i, j)

print(cnt)