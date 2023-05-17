for i in range(10):
    n = int(input())
    a, b = map(int, input().split())
    ans = a
    for j in range(b-1):
        ans = ans * a
    print(f"#{n} {ans}")