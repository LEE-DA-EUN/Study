t = int(input())
for i in range(1, t+1):
    n = int(input())
    ls = list(map(int, input().split()))
    av = sum(ls)/n
    ans = 0
    for j in range(0, len(ls)):
        if ls[j] <= av:
            ans = ans + 1
    print(f"#{i} {ans}")