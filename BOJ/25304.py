n = int(input())
t = int(input())
price = 0
for i in range(t):
    a, b = map(int, input().split())
    price = price + a * b
if n == price:
    print("Yes")
else:
    print("No")