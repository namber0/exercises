import numpy as np

def maximum(collection):
    maxNum = collection[0]
    for i in range(len(collection)):
        if collection[i] > maxNum:
            maxNum = collection[i]
    
    return maxNum

def minimum(collection):
    minNum = collection[0]
    for i in range(len(collection)):
        if collection[i] < minNum:
            minNum = collection[i]
        
    return minNum

def dividables(collection, k):
    count = 0
    for i in collection:
        if i == 0:
            continue
        if k % i == 0:
            count += 1
        
    return count

# array = np.empty(5, dtype=int)
# for i in range(len(array)):
#     array[i] = np.random.randint(100)

arrLength = int(input('enter the length of the array: '))

array = np.empty(arrLength, dtype=int)

for i in range(len(array)):
    num = int(input('enter the %i elements in the array: ' % (i + 1)))
    array[i] = num




print(list(array))
print('\nthe max number of the array is', maximum(array))
print('the min number of the array is', minimum(array))
print('the number of dividiables of 50 in the array is', dividables(array, 50))