for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(1, 10):
                for i in range(1, 10):
                    if i * (1000 * a + 100 * b + 10 * c + d) == 1000 * d + 100 * c + 10 * b + a:
                        print('a = %i, b = %i, c = %i, d = %i' % (a, b, c, d))
                        print(i)

print('end program')
                    