def symetric_difference(set1, set2):
    out = []
    for i in set1:
        for j in set2:
            if i == j:
                out.append(j);
                break;
    return out;

set1 = {'A', 'B', 'C', 'j', 'e', 'z', 'w', 'A'};
set2 = {'B', 'C', 'D', 'i', 'r', 'e', 'q', 'w', 't'};
set3 = {'b', 'a', 'e', 'B'}

print(set1, type(set1))
print(set1.intersection(set2, set3))
print(symetric_difference(set1, set2))
