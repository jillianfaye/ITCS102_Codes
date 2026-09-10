#Write a python program that accepts an integer number as age
#and determines the age group label based on that age input

name = input("Input NAME ---> ")
age = int(input("Input AGE ---> "))

print("Hi," ,name, "That age is considered as ")
if age >= 1 and age <=5:
	print("infant")
if age >= 6 and age <=12:
	print("kid")
if age >= 13 and age <=19:
	print("teenager")
if age >= 20 and age <=29:
	print("early adult")
if age >= 30 and age <=48:
	print("adult")
if age >= 49 and age <=59:
	print("advance adult")
if age >= 60 and age <=150:
	print("senior")
else:
	print("invalid")

