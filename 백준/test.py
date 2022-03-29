small_ppl = [int(input()) for i in range(9)]

total = sum(small_ppl)

for i in range(9):
    for j in range(i+1,9):
        if 100 == total - (small_ppl[i] + small_ppl[j]): 
            num1,num2=small_ppl[i],small_ppl[j]
            small_ppl.remove(num1)
            small_ppl.remove(num2)
            small_ppl.sort()
            for i in range(len(small_ppl)):
               print(small_ppl[i])
            break

    if len(small_ppl)<9:
        break
