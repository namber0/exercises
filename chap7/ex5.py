def factorial(num):
    if num == 1 or num == 0:
        return 1
    
    return num * factorial(num - 1)

def fact(num):
    out = 1
    while num >= 1:
        out *= num
        num -= 1
    return out

print(factorial(10))
print(fact(10))