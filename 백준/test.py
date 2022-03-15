n, m = map(int, input().split())

def count_number(n, k):
    count = 0
    while n:
        n //= k
        count += n
    return count

five = count_number(n, 5) - count_number(m, 5) - count_number(n-m, 5)
two = count_number(n, 2) - count_number(m, 2) - count_number(n-m, 2)

ans = min(five, two)
print(ans)