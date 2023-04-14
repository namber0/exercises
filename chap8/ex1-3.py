text = """How much wood would a woodchuck chuck
If a woodchuck could chuck wood?
He would chuck, he would, as much as he could,
And chuck as much as a woodchuck would
If a woodchuck could chuck wood."""

def textClean(text):
    text = text.replace('\n', ' '); 
    text = text.replace('?', '');
    text = text.replace('.', '');
    text = text.replace(',', '');
    return text;

text = textClean(text);
text = text.split(' ');

count = 0;

for letter in text:
    if letter == 'wood':
        count += 1;

print("the count of the letter \'wood\':", count);