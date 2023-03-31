def american_grades(grade):
    if grade > 10 or grade < 0:
        print('Wrong value')
        return ''
    if grade >= 8.5 and grade <= 10:
        return 'A'
    elif grade >= 7.5 and grade <= 8:
        return 'B'
    elif grade >= 6.5 and grade <= 7:
        return 'C'
    elif grade >= 5.5 and grade <= 6:
        return 'D'
    else:
        return 'F'
    
while True:
        grade = int(input('enter your grade: '))
        if american_grades(grade) != '':
             break

print(american_grades(grade))