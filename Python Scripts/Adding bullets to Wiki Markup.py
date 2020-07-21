#! python3
#This script adds bullet numbers to clipboard text
import pyperclip

message = pyperclip.paste().split("\n")
final = ""
for i in message:
	final += "* " + i + "\n"
pyperclip.copy(final)
