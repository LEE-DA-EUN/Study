t = int(input())
for i in range(1, t+1):
    a = list(map(int, input().split()))
    for j in range(5):
        if a[j] < 40:
            a[j] = 40
    ans = sum(a)
    print(f"#{i} {ans//5}")