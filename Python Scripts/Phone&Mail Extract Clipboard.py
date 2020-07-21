#! python3

#Phone&Mail Extract Clipboard.py - Find all phone and email id from clipboard

import pyperclip, re

#RegexObjects
phoneRegex = re.compile(r'(0|\+91)?(\s)?(\d{10})')
emailRegex = re.compile(r'[a-zA-Z0-9-_]+@[a-zA-Z0-9-_]+.[a-zA-Z]{2,4}')

#Copy clipboard Data

text = str(pyperclip.paste())
matches = []
for i in phoneRegex.findall(text):
	#print(i[2])
	matches.append(i[2])
for i in emailRegex.findall(text):
	matches.append(i)

if len(matches)>0:
	pyperclip.copy("\n".join(matches))
	print("copied to clipboard")
	print("\n".join(matches))
else:
	print("No phone or addresses found.")
	
#input()