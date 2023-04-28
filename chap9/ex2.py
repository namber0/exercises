import re

def count_words(filePath):
    wordCount = {};
    with open(filePath, 'r') as file:
        for line in file:
            words = re.split(r'\W+', line.lower());
            for word in words:
                if word not in wordCount:
                    wordCount[word] = 1;
                else:
                    wordCount[word] += 1;
    for key in sorted(wordCount.keys()):
        if key == '':
            continue;
        print(key + ': ' + str(wordCount[key]));

count_words('practice.txt');