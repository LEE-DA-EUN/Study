t = int(input())
ls = []
for i in range(t):
    ls.append(int(input()))
ans = sorted(ls)

for i in range(t):
    print(ans[i])