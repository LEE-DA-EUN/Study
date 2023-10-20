t = int(input())
ls = list(map(int, input().split()))
ans = 0
for n in ls:
    for i in range(2, n+1):
        if n % i == 0:
            if n == i:
                ans = ans + 1            
            break
print(ans)