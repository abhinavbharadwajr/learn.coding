# Basic Program to :
#       1. Get Username and Password as Strings
#       2. to Check Password Match
#       3. Validalte the Strength of the Password
#       4. Use Encryption on Strings
#       5. Use Decryption on Strings

import csv
import time
from tkinter import *

# Global Variables

passMatch = False
validPass = False
validStrCtr = 0
username = ""
password = ""
confirmPass = ""
usermatch = False

# SubRoutine to User Sign-in
def signin() :
        username = input("\n Username : ")
        if() :
                username

# subRoutine to Creat a User
def signup() :
        username = input("\n Enter Username : ")

        while validPass == False or passMatch == False :
                password = input("\n Enter your Password : ")
                confirmPass = input("\n Re-confirm your Password : ")
                if(password == confirmPass) :
                        passMatch = True
                else :
                        print("\n Passwords dosen't Match!")
                        passMatch = False
                validPass = validPassword(password, validPass)
        
        chInput = input("\n Do you want Save the Password? (Y/n) : ")
        if chInput == 'Y' :
                savePass(password)
        else :
                print("\n Username : "+username)
                print("\n Password : ", end="")
                for k in range(0, len(password)) :
                        print('*', end="")

# SubRoutine to Save Password
def savePass(passStr) :
        ecryptedPassword = encryptPass(passStr)
        print("\n Encrypting ", end="")
        for j in range(4,0,-1) :
                print(".", end="")
                time.sleep(1)
        print(" Complete!")
        print("\n Password Saved! ("+ecryptedPassword+")")

# SubRoutine to check Password Validity
def validPassword(passStr, validity) :
        splChar = ['~','`','!',' ','@','#','$','%','^','&','*','(',')','_','-','+','=','{','}','[',']','|',':',';','.',"'",'<',',','>','.','?','/']
        validity = False
        errorStr = ""
        
        if(len(passStr) < 8) :
                errorStr = "Password Length must be atleast 8 characters!"
                validity = False
        elif not any(char.isdigit() for char in passStr):
                errorStr = "Password must have at least one numeral!"
                validity = False
        elif not any(char.isupper() for char in passStr) :
                errorStr = "Password must have at least one uppercase letter!"
                validity = False
        elif not any(char.islower() for char in passStr) :
                errorStr = "Password must have at least one lowercase letter!"
                validity = False
        elif not any(char in splChar for char in passStr) :
                errorStr = "Password must have at leat one of the following Special Characters (~`! @#$%^&*()_-+={[]}]|\:;'<,>.?/)"
                validity = False
        else :
                validity = True
        
        if(validity == False) :
                print("\n Not a Valid Password! "+errorStr)
                return validity
        else :
                return validity

# SubRoutine to Encrypt Password
def encryptPass (passStr) :
        encryptedPass = ""
        for i in range(0,len(passStr)) :
                encryptedPass += chr(ord(passStr[i]) + i*10 )
                return encryptedPass

# SubRoutine to Decrypt Password
def decryptPass (passStr) :
        decryptedPass = ""
        for i in range(0,len(passStr)) :
                decryptedPass += chr(ord(passStr[i]) - i*10 )
        print("\n Decrypting ", end="")
        for j in range(4,0,-1) :
                print(".", end="")
                time.sleep(1)
        print(" Complete!")
        print("\n Username : "+username)
        print("\n Password : "+decryptedPass)


print("\n\t\t Welcome to MySpace!")
print("\n 1. Sign-in \t 2. Sign-up \t 3.Goodbye")
choiceIn = input("\n your Choice : ")

if choiceIn == 1 :
        signin()
elif choiceIn == 2 :
        signup()
elif choiceIn == 3 :
        exit