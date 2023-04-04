for a in range(1, 9):
    for b in range(0, 9):
        for c in range(0, 9):
            for d in range(1, 9):
                if 4 * (1000 * a + 100 * b + 10 * c + d) == 1000 * d + 100 * c + 10 * b + a:
                    print('a = %i, b = %i, c = %i, d = %i' % (a, b, c, d))
                    break