t = int(input())
for i in range(1, t+1):
    ls = list(input())
    sls = sorted(ls)
    if sls[0] == sls[1] and sls[2] == sls[3] and sls[0] != sls[2]:
        print(f"#{i} Yes")
    else:
        print(f"#{i} No")