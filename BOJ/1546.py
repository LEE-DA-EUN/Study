n = int(input())
ls = list(map(int, input().split()))
ls.sort()
m = ls[n-1]
score = 0
for i in range(0, n):
    score += ls[i]/m*100
print(score/n)