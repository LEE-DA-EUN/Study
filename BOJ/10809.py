t = input()
alp = 'abcdefghijklmnopqrstuvwxyz'

for i in alp:
    if i in t:
        print(t.index(i), end=" ")
    else:
        print(-1, end=" ")