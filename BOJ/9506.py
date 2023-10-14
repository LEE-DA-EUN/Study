while(1):
    num = int(input())
    if num == -1:
        break
    ls = []
    for i in range(1, num):
        if num%i == 0:
            ls.append(i)
    if sum(ls) == num:
        print(num, "=", end = " ")
        print(*ls, sep = " + ")
    else:
        print(num, "is NOT perfect.")
    
