# 오늘은 재현이의 생일이다. 재현이는 친구 N명에게 롤케이크를 1개씩 선물로 받았다. 롤케이크의 길이는 A1, A2, ..., AN이다. 재현이는 길이가 10인 롤케이크만 먹는다. 따라서, 롤케이크를 잘라서 길이가 10인 롤케이크를 최대한 많이 만들려고 한다.
# 롤케이크는 다음과 같은 과정을 통해서 자를 수 있다.
#   1. 자를 롤케이크를 하나 고른다. 길이가 1보다 큰 롤케이크만 자를 수 있다. 이때, 고른 롤케이크의 길이를 x라고 한다.
#   2. 0보다 크고, x보다 작은 자연수 y를 고른다.
#   3. 롤케이크를 잘라 길이가 y, x-y인 롤케이크 두 개로 만든다.
# 재현이는 롤케이크를 최대 M번 자를 수 있다. 이때, 만들 수 있는 길이가 10인 롤케이크 개수의 최댓값을 구하는 프로그램을 작성하시오.

import sys

N,M=map(int,sys.stdin.readline().split())

roll_cake=list(map(int,sys.stdin.readline().split()))
roll_cake=sorted(roll_cake)
roll_cake=sorted(roll_cake, key=lambda x:x%10)

count=0

for cutting in roll_cake:
    if M>0:
        if cutting<10:
            continue
        elif cutting%10==0:
            temp=(cutting//10)-1
            if temp==0:
                count+=1
            else:
                if(M>=temp):
                    count+=temp+1
                    M-=temp
                else:
                    count+=M
                    break
        else:
            temp=(cutting//10)
            if (M>=temp):
                count+=temp
                M-=temp
            else:
                count+=M
                break
    else:
        break

print(count)