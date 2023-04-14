num = int(input("enter a number: "));
def approxPi(n):
    pi = 0;
    for i in range(n):
        pi += ((-1) ** i) / (2 * i + 1);
    print(4 * pi);

approxPi(num);
