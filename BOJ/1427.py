ls = list(str(input()))
lsi = list(map(int, ls))
lsi.sort(reverse = True)
for i in range(len(lsi)):
    print(lsi[i], end='')