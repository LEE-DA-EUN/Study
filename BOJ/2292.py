n = int(input())
cnt = num = 1
while n > num:
    num += 6*cnt
    cnt += 1
print(cnt)