for i in range(1,11):
    d = int(input())
    ls = list(map(int, input().split()))
    for j in range(d):
        mn = min(ls)
        mx = max(ls)
        ls[ls.index(mx)] = ls[ls.index(mx)] - 1
        ls[ls.index(mn)] = ls[ls.index(mn)] + 1
    ans = max(ls) - min(ls)
    print(f"#{i} {ans}")