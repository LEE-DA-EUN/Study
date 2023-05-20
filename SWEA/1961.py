t = int(input())
for a in range(1, t+1):
    n = int(input())
    ls = [list(map(str, input().split())) for _ in range(n)]
    ls90 = [[0 for _ in range(n)] for _ in range(n)]
    ls180 = [[0 for _ in range(n)] for _ in range(n)]
    ls270 = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            ls90[i][j] = ls[n-1-j][i]
    
    for i in range(n):
        for j in range(n):
            ls180[i][j] = ls90[n-1-j][i]

    for i in range(n):
        for j in range(n):
            ls270[i][j] = ls180[n-1-j][i]
     
    print(f"#{a}")
    for x, y, z in zip(ls90, ls180, ls270):
        xx = ''.join(x)
        yy = ''.join(y)
        zz = ''.join(z)
        print(xx, yy, zz)