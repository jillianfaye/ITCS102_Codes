from getpass import getpass

isLogin = False

while isLogin == False:
    username = input("Input username")
    password = getpass("Input password")

    if username == "happycat" and password == "meow":
        print("Access Granted")
        isLogin = True
    else:
        print("Access Denied")
        isLogin = False