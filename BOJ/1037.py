n = int(input())
ls = list(map(int, input().split()))
ans = max(ls) * min(ls)
print(ans)