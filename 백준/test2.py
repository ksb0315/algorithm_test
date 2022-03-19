# 어린 왕자는 전문적인 해커이다. 어린 왕자는 최근에 n-bit로 이루어진 이진 암호문을 알아내기 위해 혈안이 되어 있다. 이 암호문을 알아내기 위한 단서를 한 가지 얻었는데, n개의 숫자들과 이 암호문을 이용해서 암호화된 숫자를 알아낸 것이다.
# 암호화된 숫자 K = a1t1 + a2t2 + ... + antn 으로 표현된다. 여기서 t1 ~ tn은 0 또는 1로 우리가 알아내려고 하는 n-bit의 이진 암호문을 순서대로 이루는 숫자들이다.
# 어린 왕자는 a1 ~ an과 K를 알고 있다. 이진 암호문을 알아내는 프로그램을 작성하시오.

n = int(input())
num = []
for _ in range(n):
    num.append(int(input()))
k = int(input())
bi_1 = [0 for i in range(n//2)]
bi_2 = [0 for i in range(n//2,n)]
arr_1 = list()
arr_2 = list()
for i in range(len(bi_1)):
    bi_1[i]