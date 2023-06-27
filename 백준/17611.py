# 다각형의 두 선분이 연속하는 선분의 꼭짓점을 제외하고는 만나지 않는 다각형을 단순다각형이라고 부른다. 
# 다각형의 각 변이 x축과 y축에 평행한 다각형을 직각다각형이라 부른다.
# 단순다각형이면서 직각다각형을 단순직각다각형이라 부른다. 아래 두 그림은 단순직각다각형의 예를 보여준다. 
# 단순직각다각형이 주어질 때, 
# 수평선 H가 다각형의 수직선분과 몇 번 교차하는지 또는 수직선 V가 다각형의 수평선분과 몇 번 교차하는지 알고자 한다. 
# 첫 번째 그림에서 수평선 H는 4개의 수직선분과 교차하고 수직선 V는 2개의 수평선분과 교차한다. 
# 두 번째 그림은 첫 번째 그림에서 수평선 H의 위치를 조금 위로 옮긴 것으로 8개의 수직선분과 교차하게 된다. 
# 이때, 단순직각다각형과 가장 많이 교차하는 수평선 H와 수직선 V의 위치를 찾아 그때의 교차 횟수를 구하고자 한다. 
# 단, 수평선 H는 다각형의 어떤 수평선분과도 겹처 놓여서는 안 되고, 유사하게 수직선 V는 다각형의 어떤 수직선분과도 겹쳐 놓여서는 안 된다.
# 수평선 H의 위치를 잘 정해서 주어진 단순직각다각형의 수직선분과 가장 많이 교차하는 지점을 찾을 때, 그 때의 교차 횟수를 h라 하고, 
# 유사하게 수직선 V와 주어진 단순직각다각형의 수평선분과 가장 많이 교차하는 횟수를 v라 할 때, max(h, v)를 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n = int(input())
data = []
for _ in range(n):
    data.append(input())
data.append(data[0])

num_dict_x = {}
num_dict_y = {}

pre_x, pre_y = data[0].split(' ')
pre_x, pre_y = int(pre_x), int(pre_y)
for k in range(1, len(data)):
    x, y = data[k].split(' ')
    x, y = int(x), int(y)

    if x == pre_x:
        start = min(y, pre_y)
        end = max(y, pre_y)
        if start in num_dict_y.keys():
            num_dict_y[start] += 1
        else:
            num_dict_y[start] = 1
        if end in num_dict_y.keys():
            num_dict_y[end] -= 1
        else:
            num_dict_y[end] = -1

    if y == pre_y:
        start = min(x, pre_x)
        end = max(x, pre_x)
        if start in num_dict_x.keys():
            num_dict_x[start] += 1
        else:
            num_dict_x[start] = 1
        if end in num_dict_x.keys():
            num_dict_x[end] -= 1
        else:
            num_dict_x[end] = -1

    pre_x, pre_y = x, y

num_dict_x = sorted(num_dict_x.items(), key=(lambda x:x[0]))
num_dict_y = sorted(num_dict_y.items(), key=(lambda x:x[0]))

max_x = 0
temp_x = 0
for k, v in num_dict_x:
    temp_x += v
    max_x = max(max_x, temp_x)

max_y = 0
temp_y = 0
for k, v in num_dict_y:
    temp_y += v
    max_y = max(max_y, temp_y)

print(max(max_x, max_y))