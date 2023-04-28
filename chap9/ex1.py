import re

def count_words(filePath):
    with open(filePath, 'r') as file:
        content = file.read();
        words = re.split(r'\W+', content.lower());
        wordCount = {};
        for word in words:
            if word not in wordCount:
                wordCount[word] = 1;
            else:
                wordCount[word] += 1;
        
        tmp = sorted(wordCount.keys());
        for key in tmp:
            if key == '':
                continue;
            print(key + ': ' + str(wordCount[key]));

count_words('practice.txt');