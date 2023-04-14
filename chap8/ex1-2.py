import string

reference = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
array = [];

def rot13(array):
    out = '';
    for letter in array:
        position = reference.index(letter);
        rotation = (position + 13) % len(array);
        out += reference[rotation] + ' ';

    return out;

for letter in string.ascii_uppercase:
    array.append(letter)
    print(letter, end=' ');
print('');

print(rot13(array));