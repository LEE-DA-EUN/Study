t = int(input())
for i in range(1, t+1):
    n = int(input())
    ls = []
    for j in range(n):
        p, x = map(float, input().split())
        ls.append(p*x)
    ans = sum(ls)
    print(f"#{i} {ans:.6f}")