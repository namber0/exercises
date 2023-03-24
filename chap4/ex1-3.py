num = int(input("enter number: "))
ranges = int(input("enter range: "))

def num_seperated(num, ranges):
    for i in range(1, ranges + 1):
        print("%d" % (num * i), end='')
        if i == ranges:
            break
        print("---", end='')
    print('')

num_seperated(num, ranges)