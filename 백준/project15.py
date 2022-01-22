# DNA란 어떤 유전물질을 구성하는 분자이다. 이 DNA는 서로 다른 4가지의 뉴클레오티드로 이루어져 있다(Adenine, Thymine, Guanine, Cytosine). 우리는 어떤 DNA의 물질을 표현할 때, 이 DNA를 이루는 뉴클레오티드의 첫글자를 따서 표현한다. 만약에 Thymine-Adenine-Adenine-Cytosine-Thymine-Guanine-Cytosine-Cytosine-Guanine-Adenine-Thymine로 이루어진 DNA가 있다고 하면, “TAACTGCCGAT”로 표현할 수 있다. 그리고 Hamming Distance란 길이가 같은 두 DNA가 있을 때, 각 위치의 뉴클오티드 문자가 다른 것의 개수이다. 만약에 “AGCAT"와 ”GGAAT"는 첫 번째 글자와 세 번째 글자가 다르므로 Hamming Distance는 2이다.
# 우리가 할 일은 다음과 같다. N개의 길이 M인 DNA s1, s2, ..., sn가 주어져 있을 때 Hamming Distance의 합이 가장 작은 DNA s를 구하는 것이다. 즉, s와 s1의 Hamming Distance + s와 s2의 Hamming Distance + s와 s3의 Hamming Distance ... 의 합이 최소가 된다는 의미이다.
if __name__ == '__main__':
    n, m = map(int, input().split())
    dna = []
    result = ''
    for i in range(n):
        dna.append(input())
    for i in range(m): #Hamming Distance의 합이 가장 작은 DNA
        dna_set = []
        for j in range(n):
            dna_set.append(dna[j][i])
        dna_set = list(set(dna_set))
        cnt = []
        for k in range(len(dna_set)):
            max_a = 0
            for j in range(n):
                if dna[j][i] == dna_set[k]:
                    max_a += 1
            cnt.append(max_a)
        if len(cnt) == 4:
            dna_set.sort()
        max_b = 0
        for k in range(len(cnt)):
            if cnt[k] > max_b:
                max_b = cnt[k] 
    
        a = cnt.index(max_b)
        result = result + dna_set[a]
    print(result)

    #Hamming Distance의 합
    count = 0
    for i in range(n):
        for j in range(m):
            if dna[i][j] != result[j]:
                count += 1
    print(count)
