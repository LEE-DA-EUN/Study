num = int(input())
ans = 1
while ans * (ans + 1) / 2 <= num:
    ans = ans + 1
print(ans - 1)