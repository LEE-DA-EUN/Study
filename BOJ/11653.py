n = int(input())
for i in range(2, n+2):
    if n == 1:
        break
    if n%i==0:
        while n%i == 0:
            print(i)
            n = n/i
    