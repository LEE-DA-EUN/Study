t = int(input())
ls = list(map(int,input().split()))
n = int(input())
ans = 0
for i in range(t):
    if ls[i] == n:
        ans = ans + 1

print(ans)