t = int(input())
for i in range(1, t+1):
    a = int(input())
    ls = list(map(int, input().split()))
    ls.sort()
    print(f"#{i}", end = " ")
    for j in range(0,a):
        print(ls[j], end=" ")
    print("")