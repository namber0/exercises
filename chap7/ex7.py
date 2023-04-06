num = input('enter 3 numbers: ')

num = num.split(' ')
num = [int(i) for i in num]

print('largest:', str(max(num)))
print('smallest:', str(min(num)))
print('average: %.2f' % (sum(num) / len(num)))