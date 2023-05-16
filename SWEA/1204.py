t = int(input())
for i in range(1, t+1):
    z = input()
    score = list(map(int, input().split()))
    ls = [0 for k in range(101)]
    a = []
    for j in range(0, len(score)):
        ls[score[j]-1] = ls[score[j]-1] + 1
    for l in range(0, len(ls)):
        if ls[l] == max(ls):
            a.append(l+1)
    ans = max(a)
    print(f"#{i} {ans}")