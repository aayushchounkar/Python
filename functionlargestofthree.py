#Write a python function to find maximum of three numbers

def largest():
    if num1>num2 and num1>num3:
        print("Number 1 is greater ")
    elif num1<num2 and num3<num2:
        print("Number 2 is greater ")
    elif num3>num1 and num3>num2:
        print("number 3 is greater")
    else:
        print("numbers are equal")


num1=int(input("enter a number "))
num2=int(input("enter a number "))
num3=int(input("enter a number "))
largest()