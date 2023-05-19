for i in range(1, 11):
    n = input()
    ls = []
    mx = []
    for j in range(100):
        a = list(map(int, input().split()))
        # 각 행의 합
        mx.append(sum(a))
        ls.append(a)
    # 각 열의 합
    for k in range(100):
        cs = 0
        for l in range(100):
            cs = cs + ls[l][k]
        mx.append(cs)
    # 대각선 1
    d1 = 0
    for o in range(100):
        d1 = d1 + ls[o][o]
    #대각선 2
    d2 = 0
    for x in range(100):
        y = 99-x
        d2 = d2 + ls[x][y]
    mx.append(d1)
    mx.append(d2)
    ans = max(mx)
    print(f"#{i} {ans}")