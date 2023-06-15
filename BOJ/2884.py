a, b = map(int, input().split())
if b < 45:
    t = 45 - b
    ans2 = 60 - t
    if a == 0:
        ans1 = 23
    else:
        ans1 = a - 1
else:
    ans2 = b - 45
    ans1 = a
print(ans1, ans2)
