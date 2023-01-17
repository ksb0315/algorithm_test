# 평행사변형은 평행한 두 변을 가진 사각형이다. 세 개의 서로 다른 점이 주어진다. A(xA,yA), B(xB,yB), C(xC,yC)
# 이때, 적절히 점 D를 찾아서 네 점으로 평행사변형을 만들면 된다. 이때, D가 여러 개 나올 수도 있다.
# 만들어진 모든 사각형 중 가장 큰 둘레 길이와 가장 작은 둘레 길이의 차이를 출력하는 프로그램을 작성하시오. 만약 만들 수 있는 평행사변형이 없다면 -1을 출력한다.

import sys

input = sys.stdin.readline

ax, ay, bx, by, cx, cy = map(int, input().split())

if ((ax-bx)*(ay-cy)==(ay-by)*(ax-cx)):
    print(-1.0)
    exit(0)

ab_length = ((ax-bx)**2 + (ay-by)**2)**0.5
ac_length = ((ax-cx)**2 + (ay-cy)**2)**0.5
bc_length = ((bx-cx)**2 + (by-cy)**2)**0.5

length = [ab_length+ac_length, ab_length+bc_length, ac_length+bc_length]
result = max(length) - min(length)
print(2*result)

# x1, y1, x2, y2, x3, y3 = map(int, input().split())
# axis = [[x1, y1], [x2, y2], [x3, y3]]
# axis_dist = []
# grad = []

# for i in range(3):
#     d = ((axis[i][0] - axis[i-1][0]) ** 2 + (axis[i][1] - axis[i-1][1]) ** 2) ** (1/2)
#     if axis[i][0] - axis[i-1][0] == 0:
#         grad.append(abs(axis[i][1] - axis[i-1][1])/0.00000000001)
#     else:
#         grad.append(abs(axis[i][1] - axis[i-1][1])/abs(axis[i][0] - axis[i-1][0]))
#     axis_dist.append(d)
# grad = list(set(grad))
# if len(grad) == 1:
#     print(-1)
# else:
#     sqrt_dist = []

#     for i in range(3):
#         sqrt_dist.append(2 * (axis_dist[i] + axis_dist[i-1]))

#     ans = max(sqrt_dist) - min(sqrt_dist)
#     print(ans)


# d_ind1 = dist.index(max(dist))
# d_ind2 = d_ind1 - 1

# x4 = axis[d_ind1][0]
# y4 = axis[d_ind2][1]

# temp_xy4 = [[x4, y4], [-x4, y4], [x4, -y4]]

# for i in range(3):
#     w_d = temp_xy4[i][0] - axis