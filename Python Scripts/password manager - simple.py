#! python3
# pw.py - An insecure password locker program

PASSWORDS = {'email':"ThisIsTheEmailPassword",
             'blog':"Thisistheblogpasswor"}


import sys,pyperclip
if len(sys.argv)<2:
	print ("Usage: python pw.py [account] - copy account password")
	sys.exit()
account = sys.argv[1] #first command line argv is the account name


if account in PASSWORDS:
	pyperclip.copy(PASSWORDS[account])
	print("Password copied")
else:
	print("There is no account")
	
input()