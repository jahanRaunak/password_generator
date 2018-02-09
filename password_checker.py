Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:54:40) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> import string
>>> adjectives=['raunak','surbhi','dhriti','abha']
>>> nouns=['apple','mango','guava']
>>> print('Welcome to password picker')
Welcome to password picker
>>> while True:
	print("\n Do u want to new password?(y/n)")
	ans=input()
	if ans=='y':
		adjective=random.choice(adjectives)
		noun=random.choice(nouns)
		number=random.randrange(0, 100)
		special_char=random.choice(string.punctuation)
		password=adjective + noun + str(number) + special_char
		print ('your new password is: %s ' %password)
		continue
	else:
		print("THank you for trying passwordn picker")
		exit()

		

 Do u want to new password?(y/n)
y
your new password is: raunakapple46- 

 Do u want to new password?(y/n)
y
your new password is: raunakmango70+ 

 Do u want to new password?(y/n)
