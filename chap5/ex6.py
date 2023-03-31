def give_grade(score):
    if score >= 60.0:
        grade = 'D'
    elif score >= 70.0:
        grade = 'C'
    elif score >= 80.0:
        grade = 'B'
    elif score >= 90.0:
        grade = 'A'
    else:
        grade = 'F'

    return grade

print(give_grade(80))

'''
because it uses elif and there's no ending conditions, it will only stop at the first if and then skip to the return part of the function
'''