t = int(input())
for i in range(1, t+1):
    n, a, b = map(int, input().split())
    mx = min(a,b)
    if n >= a+b:
        mn = 0
    else:
        mn = a+b-n
    print(f"#{i} {mx} {mn}")
    