t = int(input())
for i in range(t):
    n = int(input())
    for j in [25,10,5,1]:
        print(n//j,end=' ')
        n = n%j