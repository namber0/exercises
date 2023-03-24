def sum_first_int(n):
    sum = 0
    for i in range(n + 1):
        sum += i
    print(sum)

inp = int(input("enter positive integer: "))
sum_first_int(inp)