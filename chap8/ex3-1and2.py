def onlyInt():
    out = 0;
    while True:
        num = input();
        try:
            num = float(num);
            out = num;
            break;
        except ValueError:
            print('invalid input');
            pass
    return out;

myDict = {};

def enterProductAndPrice(myDict):
    while True:
        usr1 = input("enter product name: ");
        print("enter price:", end=' ');
        usr2 = onlyInt();

        myDict[usr1] = usr2;
        finish = input("are you done entering product names and prices? ");
        if finish.lower() == 'yes':
            break;
        print('');
    return myDict;


def getPrice(myDict):
    keyList = list(myDict.keys());

    while True:
        print("all the products in the dict is:", keyList);
        userKey = input("enter the product you want to check: ");
        print(myDict[userKey]);
        keyFin = input(("\nare you finished? "));
        if keyFin.lower() == 'yes':
            break;
        print('');

def getLowerPrice(myDict):
    keyList = list(myDict.keys());
    out = [];

    while True:
        print("all the products in the dict is:", keyList);
        print("enter the price you want to check:", end=' ');
        userPrice = onlyInt();
        for key in myDict:
            if myDict[key] < userPrice:
                out.append(key);
        print(out);

        keyFin = input(("\nare you finished? "));
        if keyFin.lower() == 'yes':
            break;
        print('');

enterProductAndPrice(myDict);

print('');

getPrice(myDict);

print('');

getLowerPrice(myDict);

