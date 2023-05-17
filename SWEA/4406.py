t = int(input())
for i in range(1, t+1):
    a = str(input())
    ls = ['a', 'e', 'i', 'o', 'u']
    for j in ls:
        if j in a:
            a = a.replace(j,'')
    print(f"#{i} {a}")