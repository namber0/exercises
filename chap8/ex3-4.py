users = {
    "usr1": "passwd1",
    "usr2": "passwd2",
    "usr3": "passwd3",
    "usr4": "passwd4",
    "usr5": "passwd5",
    "usr6": "passwd6",
    "usr7": "passwd7",
    "usr8": "passwd8",
    "usr9": "passwd9",
    "use10": "passwd10"
}

while True:
    username = input("enter username: ");

    if username not in users:
        print("not a valid user");
        continue;
    
    password = input("enter password: ");

    while users[username] != password:
        print("invalid password");
        password = input("enter your password: ");
    
    print("logged in");
    break;