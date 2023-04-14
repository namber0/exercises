usr = input("enter a text: ");

a, e, i, o, u = 0, 0, 0, 0, 0;

for letter in usr:
    if letter.lower() == 'a':
        a += 1;
    elif letter.lower() == 'e':
        e += 1;
    elif letter.lower() == 'i':
        i += 1;
    elif letter.lower() == 'o':
        o += 1;
    elif letter.lower() == 'u':
        u += 1;



print(f'\'a\' count: {a}\n\'e\' count: {e}\n\'i\' count: {i}\n\'o\' count: {o}\n\'u\' count: {u}');