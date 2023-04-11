while True:
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    if b > a:
        break

import math
for i in range(a, b + 1):
    for x in range(1, int(math.sqrt(i) + 1)):
            y = math.sqrt(i - x**2)
            if y == int(y) and int(y) != 0:
                print(f"{x}**2 + {y}**2 = {i}")

# if y != 0:
#     print('x is', x)
#     print('y is', y)
# else:
#     print('no suitable candidate')
