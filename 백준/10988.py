s = input()
flag = True
for i in range(len(s)//2):
    if s[i] != s[len(s)-i-1]:
        print(0)
        flag = False
        break
    
if flag:
    print(1)
