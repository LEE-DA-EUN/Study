t = int(input())
ls = []
for i in range(t):
    n = int(input())
    if n == 0:
        ls.pop()
    else:
        ls.append(n)
print(sum(ls))