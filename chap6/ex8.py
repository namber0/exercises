while True:
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    if b > a:
        break

class Found(Exception):
    pass

try:
    for i in range(a, b+1):
        for j in range(a, b+1):
            if i**2 + j**2 == b:
                raise Found
            
except Found:
    print('i is', i)
    print('j is', j)

else:
    print('i and j has no suitable candidate')
