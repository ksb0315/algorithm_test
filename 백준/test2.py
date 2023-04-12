def solution(Dir, Cmd):
    tree = []

    # for d in Dir:
    #     temp = list(d.split('/'))
    #     for t in temp:
    #         if t not in tree:
    #             tree.append(t)
    
    # print(tree)


    for cmd in Cmd:
        answer = ''
        if len(cmd) == 2:
            if cmd[0] == "CD":
                for d in Dir:
                    if cmd[1] in d:
                        temp = list(d.split('/'))
                        for t in temp:
                            if t == cmd[1]:
                                answer += t
                                break
                            else:
                                answer += (t + "/")
                        break
                
            else:
                print("Wrong Command")
        elif len(cmd) == 1 and cmd[0] == "CD":
            temp = answer
            continue
        else:
            print("Wrong Command")
    return answer


a= ["C:/root","C:/root/folder1","C:/root/folder2/file1.txt","C:/root/folder2/file2.txt"]
b= [["CD","folder1"],["CD"],["CD","folder2"]]

solution(a, b)