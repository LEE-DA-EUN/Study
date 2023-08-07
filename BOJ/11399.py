t = x = int(input())
ls = list(map(int, input().split()))
ls.sort()
ans = 0
for i in range(t):
    ans = ans + ls[i]*x
    x = x-1
print(ans)