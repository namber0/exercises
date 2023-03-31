reference = {
    3: 'Spring', 4: 'Spring', 5: 'Spring', 6: 'Summer', 7: 'Summer', 8: 'Summer', 9: 'Fall', 10: 'Fall', 11: 'Fall', 12: 'Spring', 1: 'Spring', 2: 'Spring'
}

month = int(input('enter a month: '))

while month > 12 or month <= 0:
    print("that's not a month of the year")
    month = int(input('enter a month: '))

print(reference[month])