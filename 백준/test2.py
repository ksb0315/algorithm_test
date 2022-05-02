#!/usr/bin/python3
import sys

if __name__ == '__main__':
    file_name = str(sys.argv[1])
    num = int(sys.argv[2])
    
    f=open(file_name, 'r')
    lines = []
    while True:
        line = f.readline()
        if not line: break
        line = line.rstrip()
        lines.append(line)

    f.close()
    temp=[]
    for i in range(len(lines)):
        lines[i] = lines[i].split()
        for j in range(len(lines[i])):
            lines[i][j] = ''.join(filter(str.isalnum, lines[i][j]))
            temp.append(lines[i][j])
    
    temp2 = list(temp)
    temp2 = set(temp2)
    count_list = dict()
    for word in temp2:
        count_list[word] = temp.count(word)
    count_list = sorted(count_list.items(), key= lambda x: x[1], reverse=True)
    cnt = 0
    for word, count in count_list:
        print(str(word).ljust(8), str(count).rjust(8))
        cnt+=1
        if cnt == num: break