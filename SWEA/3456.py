t = int(input())
for i in range(1, t+1):
    a, b, c = map(int, input().split())
    if a == b:
        if b == c:
            print(f"#{i} {a}")
        else:
            print(f"#{i} {c}")
    else:
        if b == c:
            print(f"#{i} {a}")
        else:
            print(f"#{i} {b}")