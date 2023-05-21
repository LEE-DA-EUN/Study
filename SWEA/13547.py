t = int(input())
for i in range(1, t+1):
    ls = list(input())
    k = len(ls)
    win = 0
    for j in range(k):
        if ls[j] == 'o':
            win = win + 1
    if win + 15 - k < 8:
        print(f"#{i} NO")
    else:
        print(f"#{i} YES")
    