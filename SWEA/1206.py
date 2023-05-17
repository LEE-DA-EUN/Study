for i in range(1, 11):
    n = int(input())
    bd = list(map(int, input().split()))
    a = [0,0,0,0]
    ans = 0
    for j in range(2, n-2):
        a[0] = bd[j] - bd[j-2]
        a[1] = bd[j] - bd[j-1]
        a[2] = bd[j] - bd[j+1]
        a[3] = bd[j] - bd[j+2]
        mn = min(a)
        if mn < 0:
            ans = ans + 0
        else:
            ans = ans + mn
    print(f"#{i} {ans}")