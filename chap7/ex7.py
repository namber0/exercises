def maximum(collection):
    maxNum = collection[0];
    for i in range(len(collection)):
        if collection[i] > maxNum:
            maxNum = collection[i];
    return maxNum;

def minimum(collection):
    minNum = collection[0]
    for i in range(len(collection)):
        if collection[i] < minNum:
            minNum = collection[i];
    return minNum;

def sumarize(collection):
    total = 0;
    for num in collection:
        total += num;
    return total;

num = input('enter 3 numbers: ');

num = num.split(' ');

# for nums in num:
#     if nums == '':
#         num.remove(nums);

num = [int(i) for i in num];

print('largest:', str(maximum(num)));
print('smallest:', str(minimum(num)));
print('average: %.2f' % (sumarize(num) / len(num)));