t = int(input())
for i in range(1, t+1):
    s = str(input())
    ls = list(s)
    l = len(ls)
    for j in range(0, l//2):
        if ls[j] != ls[l-1]:
            print(f"#{i} 0")
            break
        else:
            print(f"#{i} 1")
            break
                   