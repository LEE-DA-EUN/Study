t = int(input())
ls = []
for i in range(t):
    ans = 0
    a, b, c = map(int, input().split())
    if a == b == c:
        ans = 10000 + a * 1000
    elif a == b or a == c:
        ans = 1000 + a * 100
    elif b == c:
        ans = 1000 + b * 100
    else:
        ans = max(a,b,c) * 100
    ls.append(ans)
print(max(ls))