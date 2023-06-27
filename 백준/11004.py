# 수 N개 A1, A2, ..., AN이 주어진다. A를 오름차순 정렬했을 때, 앞에서부터 K번째 있는 수를 구하는 프로그램을 작성하시오.

import sys

input = sys.stdin.readline

n, k = map(int, input().split())
arr = sorted(list(map(int ,input().split())))
print(arr[k-1])

