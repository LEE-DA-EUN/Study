n = int(input())
if n >= 1 and n <= 1000:
    for i in range(1, n+1):
        if n % i == 0:
            print(i, end=" ")