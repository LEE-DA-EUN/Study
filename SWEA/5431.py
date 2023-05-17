t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    ls = list(map(int, input().split()))
    ans = []
    for j in range(1,n+1):
        if j not in ls:
            ans.append(j)
    print(f"#{i}", end=" ")
    for k in range(len(ans)):
        print(ans[k], end=" ")
    print()