ls = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
t = input()
ans = 0
for i in range(len(t)):
    for j in ls:
        if t[i] in j:
            ans = ans + ls.index(j) + 3
print(ans)