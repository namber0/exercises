def distinct(str1, str2):
    count = 0

    for letter in set(str1):
        if letter in str2:
            count += 1

    return count

print(distinct('rebelion', 'apple'))