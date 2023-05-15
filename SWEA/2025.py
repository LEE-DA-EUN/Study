a = int(input())
b = 0
if a <= 10000:
    for i in range(1, a+1):
        b = b + i
    print(b)