w = input().upper()
wls = list(set(w))

cnt = []
for i in wls:
    cnt.append(w.count(i))

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(wls[cnt.index(max(cnt))])