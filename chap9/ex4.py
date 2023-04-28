import re

def findCommonWords(file1, file2, file3):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(file3, 'r') as f3:
        text1 = f1.read();
        text2 = f2.read();
        text3 = f3.read();

    words1 = set(re.findall(r'\w+', text1.lower()));
    words2 = set(re.findall(r'\w+', text2.lower()));
    words3 = set(re.findall(r'\w+', text3.lower()));

    common_words = words1 & words2 & words3;

    return common_words;

commonWords = findCommonWords('file1.txt', 'file2.txt', 'file3.txt');
print(commonWords);