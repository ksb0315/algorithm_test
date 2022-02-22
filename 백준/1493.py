# 세준이는 length × width × height 크기의 박스를 가지고 있다. 그리고 세준이는 이 박스를 큐브를 이용해서 채우려고 한다. 큐브는 정육면체 모양이며, 한 변의 길이는 2의 제곱꼴이다. (1×1×1, 2×2×2, 4×4×4, 8×8×8, ...)
# 세준이가 가지고 있는 박스의 종류와 큐브의 종류와 개수가 주어졌을 때, 박스를 채우는데 필요한 큐브의 최소 개수를 출력하는 프로그램을 작성하시오.

length, width, height = map(int, input().split())
n = int(input())
cube = [list(map(int, input().split())) for _ in range(n)]
volume = length * width * height
ans = 0
before = 0
cube.sort(reverse=True)

for w, cnt in cube:
    before <<= 3
    v = 2 ** w
    maxCnt = (length // v) * (width // v) * (height // v) - before
    maxCnt = min(cnt, maxCnt)
    ans += maxCnt
    before += maxCnt

if before == volume:
    print(ans)
else:
    print(-1)