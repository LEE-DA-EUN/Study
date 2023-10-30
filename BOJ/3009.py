xls = []
yls = []
for i in range(3):
    x, y = map(int, input().split())
    xls.append(x)
    yls.append(y)

for i in range(3):
    if xls.count(xls[i]) == 1:
        xans = xls[i]
    if yls.count(yls[i]) == 1:
        yans = yls[i]
print(xans, yans)