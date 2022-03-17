case = int(input())
ans = []
for _ in range(case):
    string = list(input().split())
    for i in range(len(string)):
        temp = ''
        for j in range(len(string[i])-1, -1, -1):
            temp += string[i][j]
        string[i] = temp
    ans.append(' '.join(string))
for i in ans:
    print(i)