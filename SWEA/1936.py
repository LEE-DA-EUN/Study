A, B = map(int, input().split())
if A == 1 and B == 2:
    print("B")
if A == 1 and B == 3:
    print("A")
if A == 2:
    if B == 1:
        print("A")
    if B == 3:
        print("B")
if A == 3:
    if B == 1:
        print("B")
    if B == 2:
        print("A")