# n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있다. 
# 이와 같은 이진 트리의 인오더와 포스트오더가 주어졌을 때, 프리오더를 구하는 프로그램을 작성하시오.

import sys

sys.setrecursionlimit(10 ** 5)
input = sys.stdin.readline

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

pos = [0] * (n + 1)
for i in range(n):
    pos[inorder[i]] = i

def preorder(in_s, in_e, post_s, post_e):
    if (in_s > in_e) or (post_s > post_e):
        return
    
    root = postorder[post_e]
    
    left_t = pos[root] - in_s
    right_t = in_e - pos[root]
    
    print(root, end = " ")
    preorder(in_s, in_s + left_t - 1, post_s, post_s + left_t - 1)
    preorder(in_e - right_t + 1, in_e, post_e - right_t, post_e - 1)

preorder(0, n - 1, 0, n - 1)