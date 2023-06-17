def divAbleBy3711(arr):
    out = [];
    for num in arr:
        if num % 3 == 0 and num % 7 == 0 and num % 11 == 0:
            out.append(num);
    return out;

def divAble37Not11(arr):
    out = [];
    for num in arr:
        if num % 3 == 0 and num % 7 == 0 and num % 11 != 0:
            out.append(num);
    return out;

def notDivAbleTo3711(arr):
    out = [];
    for num in arr:
        if num % 3 != 0 and num % 7 != 0 and num % 11 != 0:
            out.append(num);
    return out;

nums = list(range(1, 1001))

print("the numbers that are dividable by 3, 7, 11:", divAbleBy3711(nums))
print('')
print("the numbers that are dividable by 3, 7 but not 11:", divAble37Not11(nums));
print('')
print("the numbers that are not dividable by 3, 7, 11:", notDivAbleTo3711(nums));
