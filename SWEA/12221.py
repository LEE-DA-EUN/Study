t = int(input())
for i in range(1, t+1):
    a, b = map(int, input().split())
    if a < 1 or a > 9 or b < 1 or b > 9:
        print(f"#{i} -1")
    else:
        print(f"#{i} {a*b}")