n, x = map(int, input().split())
ls = list(map(int, input().split()))
for i in range(len(ls)):
    if ls[i] < x:
        print(ls[i], end=' ')