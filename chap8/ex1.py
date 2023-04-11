def bubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j];
    return array;


def reverseList(array):
    return array[::-1];

def contain5(array):
    for i in array:
        if i == 5:
            return "Yes";
    return "No";

def numberOf5s(array):
    count = 0;
    for i in array:
        if i == 5:
            count += 1;
    return count;

def removeFirstAndLast(array):
    return bubbleSort(array[1:len(array) - 1]);

def lessThan5(array):
    count = 0;
    for i in array:
        if i < 5:
            count += 1;
    return count;

arr = []

length = int(input("enter length of list: "));

for i in range(length):
    print("enter element %s:" % str(i + 1), end=' ');
    num = int(input());
    arr.append(num);

print("total number of elements in the list is:", length);

print("reverse list is:", reverseList(arr));

print("does this list contain number 5:",contain5(arr));

print("dhe number of number 5:", numberOf5s(arr));

print("demoved the first and last element and sorted the list:", removeFirstAndLast(arr));

print("number of elements that are less than 5:", lessThan5(arr));