def fibonacci(maximum):
    first, second = 1, 1
    print(first)
    print(second)
    # for i in range(ranges - 2):
    while second <= maximum:
        if first + second > maximum:
            break

        tmp = second
        second = first + second
        first = tmp

        print(second)


fibonacci(100)