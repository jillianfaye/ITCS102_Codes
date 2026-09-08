import getpass

username = 'suntukan_tau'
password = 'right_neow'

u = input("Enter Username ----> ")
p = getpass.getpass("Enter Password ----> ")

if username == u and password == p :
	print("ACCESS GRANTED")
else:
	print("ACCESS DENIED")