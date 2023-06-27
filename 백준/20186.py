# N개의 자연수가 좌우로 배열되어 있다. 여러분은 이 중 K개를 골라야 한다. 고를 때는 K개 모두를 한번에 골라야 한다.
# 여러분이 고른 수 각각에 대해서 그 수의 점수를 계산할 것이다. 
# 점수는 자신의 수에서 자신의 왼쪽에 있는 수 중 선택된 수의 개수를 뺀 값이다. 
# 이렇게 고른 수 각각에 그 점수를 계산한 후 전체점수는 계산된 점수들의 합이다. 
# 여러분은 전체점수가 최대가 되도록 K개의 수를 골라야 한다.
# 예를 들어서, N = 5개의 자연수가 순서대로 2 3 1 2 1 로 주어지고, K = 3이라고 하자. 만약 첫 번째 2와 두 개의 1을 골랐다면, 각 수의 점수를 계산해서 나열하면 2 0 −1과 같다. 
# 따라서 전체 점수는 1이다. 만약 첫 번째 2와 3, 그리고 두 번째 2를 고르고, 각 수의 점수를 계산해서 나열하면, 2 2 0과 같다.
# 따라서 전체점수는 4이다. 이 예에서 전체점수의 최댓값은 4이다.
# N개의 자연수 배열과 양의 정수 K가 주어질 때, 전체점수의 최댓값을 출력하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = sorted(list(map(int,input().split())))
sum = 0

for i in range(1,k+1):
    sum += arr[-i] - i + 1
print(sum)