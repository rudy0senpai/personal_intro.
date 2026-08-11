#Print
print("Hello Mister")
#Data Input Here
data=input('Enter name, age, branch:').split()
ID=input('What is your ID number :')
hobby=input('What is your Hobby :')
lang=input('Which Code language you are using :')
#String Declerate Below
name=data[0]
age=data[1]
branch=data[2]
#Displaying String
print(f'Welcome {name}')
print(f'Your age is {age} and you are B-tech {branch} student')
#Questions
print("The ID number is :",ID)
print("Your Hobby is :",hobby)
print("The code language is in :",lang)