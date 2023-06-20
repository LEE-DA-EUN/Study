a = b = 100
t = int(input())
for i in range(t):
    x, y = map(int, input().split())
    if x > y:
        b = b - x
    elif y > x:
        a = a - y
print(a)
print(b)