# 이진 트리를 입력받아 전위 순회(preorder traversal), 중위 순회(inorder traversal), 후위 순회(postorder traversal)한 결과를 출력하는 프로그램을 작성하시오.
# 예를 들어 위와 같은 이진 트리가 입력되면,
# 전위 순회한 결과 : ABDCEFG // (루트) (왼쪽 자식) (오른쪽 자식)
# 중위 순회한 결과 : DBAECFG // (왼쪽 자식) (루트) (오른쪽 자식)
# 후위 순회한 결과 : DBEGFCA // (왼쪽 자식) (오른쪽 자식) (루트)

import sys

input = sys.stdin.readline

match = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
m = {}
for i in range(len(match)):
    m[match[i]] = i

def preorder(node):
    global tree
    if node =='.':
        return
    print(node, end='')
    preorder(tree[m[node]][0])
    preorder(tree[m[node]][1])

def inorder(node):
    global tree
    if node =='.':
        return
    inorder(tree[m[node]][0])
    print(node, end='')
    inorder(tree[m[node]][1])

def postorder(node):
    global tree
    if node =='.':
        return
    postorder(tree[m[node]][0])
    postorder(tree[m[node]][1])
    print(node, end='')

n = int(input())
tree = [[] for _ in range(n)]

for _ in range(n):
    x, y, z = input().rstrip().split(' ')
    tree[m[x]].append(y)
    tree[m[x]].append(z)

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()