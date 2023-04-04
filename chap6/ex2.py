i = 1
while i <= 9:
    j = 1
    while j <= 10:
        num = i * j
        print('%i' % num, end=' ')
        num = i
        j += 1
    print('')
    i += 1
