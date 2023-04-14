from math import e

for i in range(-1, 4):
    if i == 0:
        print(f'e^0 = %i' % e**0);
        continue;
    print(f'e^{i} = %.5f' % e**i);
