def solution(s):
    lens = len(s)
    t = list(set(s))
    temp = []
    for i in range(len(t)):
        temp.append(t[i]*2)
    # print(temp)
    while s:
        for i in range(len(temp)):
            if temp[i] in s:
                s.replace(temp[i], '', s.count(temp[i]))

            
    


solution("baabaa")
# solution("cbcb")