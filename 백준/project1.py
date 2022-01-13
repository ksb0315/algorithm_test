#--그리디 알고리즘--
#준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
#동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

#첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
#둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

n, k = input().split()
units = []
for i in range(0,int(n)):
    unit = input()
    units.append(int(unit))
units.sort()
cnt = 0
for i in range(0,int(n)):
    unit_pop = units.pop()
    if int(k) // int(unit_pop) > 0:
        cnt += (int(k) // int(unit_pop))
        k = int(k) % int(unit_pop)
    else:
        pass

print(cnt)


# 입력값1:
# 10 4200
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000
# 출력값1: 6