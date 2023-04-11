import random

def secondLargest(arr):
    large = arr[0];
    for i in arr:
        if i > large and i < max(arr):
            large = i;
    return large;

def secondSmallest(arr):
    small = arr[0];
    for i in arr:
        if i < small and i > min(arr):
            small = i;
    return small;

def evenNums(arr):
    count = 0;
    for i in arr:
        if i % 2 == 0:
            count += 1;
    return count;

arr = []

for i in range(100):
    arr.append(random.randint(1,100));

print(arr);

print("largest value:", max(arr));
print("smallest value:", min(arr));

print("second largest value:", secondLargest(arr));
print("second smallest value:", secondSmallest(arr));

print("number of even numbers:", evenNums(arr));