i = 99
while i > 0:
    if i == 2:
        print('2 bottles of beer on the wall, 2 bottles of beer. Take one down, pass it around. 1 bottle of beer on the wall')
        i -= 1
        continue
    if i == 1:
        print('1 bottle of beer on the wall, 1 bottle of beer. Take one down, pass it around. 0 bottle of beer on the wall')
        break


    print('%i bottles of beer on the wall, %i bottles of beer. Take one down, pass it around. %i bottles of beer on the wall' % (i, i, i - 1))

    i -= 1