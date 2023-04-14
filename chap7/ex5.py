def factorial(num):
    if num == 1 or num == 0:
        return 1;
    
    return num * factorial(num - 1);

def fact(num):
    out = 1
    while num >= 1:
        out *= num;
        num -= 1;
    return out;

def binomial(n, k):
    return fact(n) / (fact(k) * fact(n - k));

# print(factorial(10));
print(fact(10));
print(binomial(10, 2));
