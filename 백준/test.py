# 2018115741 허준수 , 완료
"""
1. 가장 작은 y값 (2차원 배열)을 점 p로 시작
최초로 convex hull에 포함하는 점 p는 y 값이 가장 작은 점 중 x 값이 가장 큰 점
2. 각도를 보며(arctan()사용해서 각도구하기) 추가
math.atan2(ay – py, ax – px)가 radian 단위로 각도 반환해준다.
3. p를 제외한 각도를 오름차순으로 정렬한다 즉 P배열에 1~N에 저장되어있다.
4. 스택에 p와 P[1]를 push한다.

5. 비교(볼록, 오목)해서 볼록아니면 j는 잘못된 연결, i-k 직직연결(배열추가 삭제?)
6. N개만큼(튜플 수) 반복(push)한다. 
7. 마지막 세 점의 concave(오목) 여부 확인
"""

import math


def ccw(i, j, k):  # 반시계방향
    area2 = (j[0] - i[0]) * (k[1] - i[1]) - (j[1] - i[1]) * (k[0] - i[0])
    if area2 > 0:
        return True
    else:
        return False


def grahamScan(points):
    stack = []

    # 가장 작은 y값 구하기 위해 정렬
    points = sorted(points, key=lambda p: (p[1], -p[0]))

    # 1. 가장 작은 y값을 점 p로 시작   -- (3, -1)
    p = points[0]  # px = p[0] , py = p[1]

    # 2. 각도를 보며(arctan()사용해서 각도구하기) 추가 math.atan2(ay – py, ax – px)가 radian 단위로 각도 반환해준다.
    # 3. p를 제외한 각도를 오름차순으로 정렬한다 즉 P배열에 1~N에 저장되어있다.
    points.sort(key=lambda i: math.atan2(i[1] - p[1], i[0] - p[0]))

    # 4. 스택에 p와 P[1]를 push한다.
    stack.append(p)  # points[0]  ,  N = 0
    stack.append(points[1])        # N = 1
    next_cnt = 2                   # N = 2

    # 5. 비교(볼록, 오목)해서 볼록아니면 j는 잘못된 연결, i-k 직직연결(배열추가 삭제?)
    # 6. N개만큼(튜플 수) 반복(push)한다.
    while next_cnt < len(points):  # 2 ~ N 까지 검사
        while len(points) >= 2:  # 스택에 2개 이상 있다면
            second = stack.pop()
            first = stack[-1]

            # 7. 마지막 세 점의 concave(오목) 여부 확인
            if ccw(first, second, points[next_cnt]) == True:
                stack.append(second)
                break

        # ccw에서 볼록해서 True를 받고 세 점 중에 끝점인 points[next_cnt]를 스택에 넣어준다.
        stack.append(points[next_cnt])
        next_cnt += 1   # 다음 N을 찾기 위해 next_cnt를 증가시켜준다.

    return stack


if __name__ == "__main__":
    # xy 좌표계에 속한 점의 list(points)를 입력으로 받는 함수 정의
    list = [(0, 0), (-2, -1), (-1, 1), (1, -1), (3, -1), (-3, -1)]
    print(grahamScan(list))  # page 51

    list = [(4, 2), (3, -1), (2, -2), (1, 0), (0, 2), (0, -2), (-1, 1),
            (-2, -1), (-2, -3), (-3, 3), (-4, 0), (-4, -2), (-4, -4)]
    print(grahamScan(list))  # page 52
