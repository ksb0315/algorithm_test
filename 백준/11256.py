# 당신은 사탕 공장의 주인이다. 날마다, 당신은 J개의 사탕을 가게에 보내기 위해 상자에 포장해야 한다.
# 당신은 크기가 다른 상자 N개를 가지고 있다. 당신은 편리를 위해 상자를 최소한으로 쓰려고 한다. (박스를 다 채울 필요는 없다. 일부분만 채워도 된다.)
# 당신이 공장에서 나오는 사탕의 개수와 각 상자의 크기를 입력받고, 상자를 최소한으로 쓸 때의 사용되는 상자 개수를 출력하는 프로그램을 작성하라. 사탕들을 포장할 공간은 충분하다는 것이 보장된다.

case = int(input())
ans = []
for _ in range(case):
    cnt = 0
    candy, box = map(int,input().split())
    box_size = []
    for _ in range(box):
        x, y = map(int,input().split())
        box_size.append(x*y) 
    while candy > 0:
        big_box = box_size.pop(box_size.index(max(box_size)))
        candy -= big_box
        cnt+=1
    ans.append(cnt)

for res in ans:
    print(res)

    