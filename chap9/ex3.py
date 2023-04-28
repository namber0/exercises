contents = open("XXXX.txt", 'r');
vowels = ["o", "a", "e", "u", "i"];
tmp = open("XXXX.tmp", "w");

while True:
    content = contents.readline();
    if content == "":
        break;

    for char in content:
        if char in vowels:
            content = content.replace(char, "");
    tmp.write(content);

contents.close();
tmp.close();
print("finished copying content");

