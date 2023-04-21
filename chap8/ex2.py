import random

def average(arr):
    sums = 0;
    for i in arr:
        sums += i;
    return int(sums / len(arr));

def secondLargest(arr):
    sets = set(arr);
    maxi = max(sets);
    index = arr.index(maxi);
    arr.remove(maxi);
    scndMax = max(sets);
    arr.insert(index, maxi);
    return scndMax;

def secondSmallest(arr):
    sets = set(arr);
    mini = min(sets);
    index = arr.index(mini);
    arr.remove(mini);
    scndMin = min(sets);
    arr.insert(index, mini);
    return scndMin;

def evenNums(arr):
    count = 0;
    for i in arr:
        if i % 2 == 0:
            count += 1;
    return count;

arr = []

for i in range(20):
    arr.append(random.randint(1,101));

print(arr);

print("average of array:", average(arr));

print("largest value:", max(arr));
print("smallest value:", min(arr));

print("second largest value:", secondLargest(arr));
print("second smallest value:", secondSmallest(arr));

print("number of even numbers:", evenNums(arr));