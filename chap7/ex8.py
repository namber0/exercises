from math import e

def ePow():
    for i in range(-1, 4):
        if i == 0:
            print(f'e^0 = %i' % e**0);
            continue;
        print(f'e^{i} = %.2f' % e**i);
        print('e^{} = {:.2f}'.format(i, e**i))

ePow();
