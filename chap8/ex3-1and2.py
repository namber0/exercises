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
        finish = input("are you finished? ");
        if finish.lower() == 'yes' or finish.lower() == 'y':
            break;
    return myDict;


def getPrice(myDict):
    print();
    keyList = list(myDict.keys());

    while True:
        print("all the products in the dict is:", keyList);
        userKey = input("enter the product you want to check: ");
        print(myDict[userKey]);
        keyFin = input(("are you finished? "));
        if keyFin.lower() == 'yes' or keyFin.lower() == 'y':
            break;

def getLowerPrice(myDict):
    print();
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

        keyFin = input(("are you finished? "));
        if keyFin.lower() == 'yes' or keyFin.lower() == 'y':
            break;

enterProductAndPrice(myDict);
getPrice(myDict);
getLowerPrice(myDict);

