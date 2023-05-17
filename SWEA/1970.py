t = int(input())
for i in range(1, t+1):
    n = int(input())
    ans = []
    ans.append(n//50000)
    n = n%50000
    ans.append(n//10000)
    n = n%10000
    ans.append(n//5000)
    n = n%5000
    ans.append(n//1000)
    n = n%1000
    ans.append(n//500)
    n = n%500
    ans.append(n//100)
    n = n%100
    ans.append(n//50)
    n = n%50
    ans.append(n//10)
    n = n%10
    print(f"#{i}")
    print(*ans)