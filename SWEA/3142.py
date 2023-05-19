t = int(input())
for i in range(1, t+1):
    n, m = map(int, input().split())
    a = n-m
    b = m-a
    print(f"#{i} {b} {a}")