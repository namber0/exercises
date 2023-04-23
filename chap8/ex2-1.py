def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2;

        left = arr[:mid];
        right = arr[mid:];
        
        mergeSort(left);
        mergeSort(right);

        i = j = k = 0;

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i];
                i += 1;
            else:
                arr[k] = right[j];
                j += 1;
            k += 1;

        while i < len(left):
            arr[k] = left[i];
            i += 1;
            k += 1;

        while j < len(right):
            arr[k] = right[j];
            j += 1;
            k += 1;
    return arr;

def reverseList(array):
    return array[::-1];

def contain5(array):
    for i in array:
        if i == 5:
            return "yes";
    return "no";

def numberOf5s(array):
    count = 0;
    for i in array:
        if i == 5:
            count += 1;
    return count;

def removeFirstAndLast(array):
    return mergeSort(array[1:-1]);

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

print("the number of number 5:", numberOf5s(arr));

print("removed the first and last element and sorted the list:", removeFirstAndLast(arr));

print("number of elements that are less than 5:", lessThan5(arr));