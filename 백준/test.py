string_list = [{'a':1}, {'b':2}, {'c':3, 'd': 4}]
temp = []
dic = {}
for s in string_list:
    k = list(s.keys())
    v = list(s.values())
    for i in range(len(k)):
        temp.append(k[i])
        temp.append(v[i])
for i in range(0,len(temp),2):
    dic[temp[i]] = temp[i+1]
print(dic)