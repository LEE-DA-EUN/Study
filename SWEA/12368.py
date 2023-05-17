t = int(input())
for i in range(1, t+1):
    a, b= map(int, input().split())
    h = a+b
    ans = h%24
    print(f"#{i} {ans}")