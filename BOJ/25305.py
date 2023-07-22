n, k = map(int, input().split())
ls = list(map(int, input().split()))
sls = sorted(ls)
print(sls[n-k])