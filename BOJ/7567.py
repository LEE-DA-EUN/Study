ls = list(input())
a = ls[0]
ans = 10
for i in range(1, len(ls)):
    if a != ls[i]:
        a = ls[i]
        ans = ans + 10
    else:
        ans = ans + 5
print(ans)