# 상근이와 선영이는 학교 숙제로 로봇을 만들고 있다. 로봇을 만들던 중에 구멍을 막을 두 레고 조각이 필요하다는 것을 깨달았다.
# 구멍의 너비는 x 센티미터이고, 구멍에 넣을 두 조각의 길이의 합은 구멍의 너비와 정확하게 일치해야 한다. 정확하게 일치하지 않으면, 프로젝트 시연을 할 때 로봇은 부수어질 것이고 상근이와 선영이는 F를 받게 된다. 구멍은 항상 두 조각으로 막아야 한다.
# 지난밤, 상근이와 선영이는 물리 실험실에 들어가서 레고 조각의 크기를 모두 정확하게 재고 돌아왔다. 구멍을 완벽하게 막을 수 있는 두 조각을 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        lego = []
        for _ in range(n):
            lego.append(int(input()))
        lego.sort()
        l = 0
        r = n-1
        flag = True

        while l < r:
            if lego[l] + lego[r] == x:
                flag = False
                print("Yes " + str(lego[l]) + " " + str(lego[r]))
                break
            elif lego[l] + lego[r] > x:
                r -= 1
            else:
                l += 1

        if flag:
            print("danger")
    except:
        break

import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        lego = [int(input()) for _ in range(n)]
        lego.sort()
        i, j = 0, n-1
        flag = True
        while i < j:
            if lego[i] + lego[j] == x:
                print('yes %d %d' %(lego[i], lego[j]))
                flag = False
                break

            elif lego[i] + lego[j] < x:
                i += 1
            else:
                j -= 1
        if flag:
            print('danger')
    except:
        break