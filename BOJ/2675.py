t = int(input())
for i in range(t):
    a, b = input().split()
    n = int(a)
    for j in b:
        print(j*n, end='')
    print()