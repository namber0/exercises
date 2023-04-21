def symetric_difference(set1, set2):
    out = []
    for i in set1:
        for j in set2:
            if i == j:
                out.append(j);
                break;
    return out;

arr1 = ['A', 'B', 'C', 'j', 'e', 'z', 'w'];
arr2 = ['B', 'C', 'D', 'i', 'r', 'e', 'q', 'w', 't'];

print(symetric_difference(arr1, arr2))