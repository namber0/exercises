listDicts = [
    {'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
    {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
    {'name':'Princess', 'phone':'555-3141', 'email':''},
    {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}
]

def endsWith8(arr):
    tmp = [];
    for element in arr:
        if element['phone'][-1] == '8':
            tmp.append(element['name']);
    return tmp;

def noEmail(arr):
    tmp = [];
    for element in arr:
        if element['email'] == '':
            tmp.append(element['name']);
    return tmp;

print(endsWith8(listDicts));
print(noEmail(listDicts));
