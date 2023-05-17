import math

t = int(input())
for i in range(1, t+1):
    n, k = map(int, input().split())
    ls=[]
    hj = ['D0', 'C-', 'C0', 'C+', 'B-', 'B0', 'B+', 'A-', 'A0', 'A+']
    for j in range(n):
        a, b, c = map(int, input().split())
        score = a*35 + b*45 + c*20
        ls.append(score)
    kscore = ls[k-1]
    sls = sorted(ls)
    rank = sls.index(kscore)+1
    x = math.ceil(rank/(n/10))
    print(f"#{i} {hj[x-1]}")
        