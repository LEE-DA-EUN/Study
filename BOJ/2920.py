ls = list(map(int, input().split()))
if ls == sorted(ls):
    print("ascending")
elif ls == sorted(ls, reverse = True):
    print("descending")
else:
    print("mixed")