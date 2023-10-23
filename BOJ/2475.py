ls = list(map(int, input().split()))
sum = ans = 0
for i in range(5):
    sum += ls[i] * ls[i]

ans = sum % 10
print(ans)