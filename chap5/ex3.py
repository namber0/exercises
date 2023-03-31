reference = {
    1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31
}

while True:
    month = int(input('enter a month: '))

    if month not in reference:
        print("that's not a month of the year")
    else:
        print(str(reference[month]) + ' days')
        break
