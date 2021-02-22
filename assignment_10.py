# Cheryllynn Matos
# CIS 245 Assignment 10
# 02/21/2021

import os

user_directory = input("Enter the directory you would like to save the file in (' ') ")
filePath = user_directory

user_file = input("Enter the file name (' ') ")
fileName = user_file

completePath = filePath+fileName

if os.path.isdir(filePath):
    print("Directory exists.")

user_name = input("Enter the name: ")
user_address = input("Enter the address: ")
user_number = input("Enter the phone number: ")

with open(completePath, 'w') as fileHandle:
    fileHandle.write(user_name)
    fileHandle.write(user_address)
    fileHandle.write(user_number)

with open(completePath, 'r') as fileHandle:
    data = fileHandle.read()
    print(data)

