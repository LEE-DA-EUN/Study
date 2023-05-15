t = int(input())
md = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for i in range(1, t+1):
    a, b, c, d = map(int, input().split())
    ans = 0
    for j in range(a, c):
        ans = ans + md[j]
    x = ans - b + d + 1
    print(f"#{i} {x}")