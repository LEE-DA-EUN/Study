ls = []
for i in range(10):
    ls.append(int(input())%42)
    ans = list(set(ls))
print(len(ans))