t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    ls = []
    for j in range(0, n):
        a = list(map(int, input().split()))
        ls.append(a)
    nls = []
    for k in range(0,n-m+1):
        for l in range(0, n-m+1):
            num = 0
            for x in range(k, m+k):
                for y in range(l, m+l):
                    num = num + ls[x][y]
            nls.append(num)
    nmax = max(nls)
    print(f"#{i} {nmax}")