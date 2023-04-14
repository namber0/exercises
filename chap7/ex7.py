def bubbleSort(collection):
    for i in range(len(collection)):
        for j in range(len(collection) - i - 1):
            if collection[j] > collection[j + 1]:
                collection[j], collection[j + 1] = collection[j + 1], collection[j];

    return collection;

def maximum(collection):
    collection = bubbleSort(collection);
    return collection[-1];

def minimum(collection):
    collection = bubbleSort(collection);
    return collection[0];

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
