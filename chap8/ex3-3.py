def months31days():
    monthsWith31days = [];
    for keys in reference:
        if reference[keys] == 31:
            monthsWith31days.append(keys);
    return monthsWith31days;

def keyValueSorted(reference):
    sortedDict = sorted(reference.items(), key=lambda x:x[1]);
    return sortedDict;

reference = {
    'january':31,
    'february':28,
    'march':31,
    'april':30,
    'may':31,
    'june':30,
    'july':31,
    'august':31,
    'september':30,
    'october':31,
    'november':30,
    'december':31
}

keyList = list(reference.keys());


usr = input("enter month name: ");
print(reference[usr.lower()]);

print("keys sorted in alphabetical order:", sorted(keyList));

print("months with 31 days:", months31days());

print("months sorted by days:", keyValueSorted(reference))