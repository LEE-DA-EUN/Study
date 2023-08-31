a, b = map(int, input().split())
ab = a*b
while b:
    if a > b:
        a, b = b, a
    b = b%a
ans = ab//a
print(ans)
