t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    sl = list(map(int, input().split()))
    score = sorted(sl, reverse = True)
    ans = 0
    for j in range(0,k):
        ans = ans + score[j]
    print(f"#{i} {ans}")