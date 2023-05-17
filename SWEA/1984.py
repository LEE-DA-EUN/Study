t = int(input())
for i in range(1, t+1):
    ls = list(map(int, input().split()))
    a = sum(ls) - max(ls) - min(ls)
    ans = round(a/8)
    print(f"#{i} {ans}")