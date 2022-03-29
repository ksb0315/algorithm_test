# 창영이는 후손들에게 물려주기 위해서, 만든 트리를 항상 종이에 적어놓는다. 이때, 트리를 프리오더 순회한 결과와 인오더로 순회한 결과를 적어 놓는다. 위의 트리를 프리오더로 순회하면 DBACEGF가 되고, 인오더로 순회하면 ABCDEFG가 된다. 
# 창영이는 이 두 순서만 있으면, 트리를 만들 수 있다고 생각했기 때문에, 포스트오더로 순회한 결과는 적지 않았다.
# 몇 년이 지난 후, 종이를 보고 트리를 다시 만들려고 했다. 하지만 너무 귀찮은 나머지 프로그램을 작성하려고 한다. 트리를 프리오더와 인오더로 순회한 결과가 주어졌을 때, 포스트오더로 순회한 결과를 구하는 프로그램을 작성하시오.

def post(pre, inorder):
    global ans
    if not pre: return
    root = pre[0]
    if type(inorder) is int:
        inorder = [inorder]
    l = inorder.index(root)
    post(pre[1:l+1], inorder[:l])
    post(pre[l+1:], inorder[l+1:])
    ans += str(root)


while True:
    ans = ''
    pre,inorder = map(list,input().split())
    post(pre, inorder)
    print(ans)
    