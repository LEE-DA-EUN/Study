for j in range(0, 5):
    for i in range(0, 5):
        if i == j:
            print("#", end="")
        else:
            print("+", end="")
    print("\n")