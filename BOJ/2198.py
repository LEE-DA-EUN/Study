a, b = input().split()
ar = int(a[::-1])
br = int(b[::-1])
if ar > br:
    print(ar)
else:
    print(br)