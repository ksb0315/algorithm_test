# 도현이네 반 학생 N명의 이름과 국어, 영어, 수학 점수가 주어진다. 이때, 다음과 같은 조건으로 학생의 성적을 정렬하는 프로그램을 작성하시오.
# 국어 점수가 감소하는 순서로
# 국어 점수가 같으면 영어 점수가 증가하는 순서로
# 국어 점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전 순으로 증가하는 순서로 (단, 아스키 코드에서 대문자는 소문자보다 작으므로 사전순으로 앞에 온다.)

import sys

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b, c, d = input().rstrip().split(" ")
    arr.append([a, int(b), int(c), int(d)])
arr.sort(key= lambda x: x[0])
arr.sort(key= lambda x: x[3],reverse= True)
arr.sort(key= lambda x: x[2])
arr.sort(key= lambda x: x[1],reverse= True)
for a in arr:
    print(a[0])