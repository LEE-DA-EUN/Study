t = int(input())
md = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
for i in range(1, t+1):
    m, d = map(int, input().split())
    day = 0
    for j in range(1, m):
        day = day + md[j]
    ans = day + d + 3
    a = ans%7
    print(f"#{i} {a}")