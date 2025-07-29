## managment system 
from datetime import datetime
#Input patient details
Name= input("Enter Paitent Name:")
DoB= input("Enter date of Birth(YYYY-MM-DD):")
Mobile_No = input("Enter mobile NUmber:")
Batch_No = int(input("enter batch no.:"))


# create a dictionary to store data
Data = {
    "Name" : Name,
    "Date Of Birth" : DoB,
    "Mobile Number" : Mobile_No,
    "Batch Number"  : Batch_No
}

#Check if all data is entered
if all(Data.value()):
    print("All data entered")
else: 
    print("Some error found")
