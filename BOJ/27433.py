n = int(input())
for i in range(0, n+1):
    if i == 0:
        ans = 1
    else:
        ans = ans * i
print(ans)