n = int(input())
ans = 0
for i in range(1, n+1):
    num = sum(map(int, str(i)))
    ans = i + num
    if ans == n:
        print(i)
        break
    if i == n:
        print(0)
