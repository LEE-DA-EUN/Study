t = int(input())
for i in range(1, t+1):
    ls = list(map(int, input().split()))
    a = 0
    for j in range(0, len(ls)):
        n = ls[j]
        if n%2 == 1:
            a = a + n
    print(f"#{i} {a}")