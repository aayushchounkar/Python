num1=int(input("Enter a number1="))
num2=int(input("Enter a number2="))
num3=int(input("Enter a number3="))

if num1>num2 and num1>num3:
    print (num1,"Is the greater among all")

elif num2>num1 and num2>num3:
    print(num2,"Is greater among all")

elif num3>num1 and num3>num2:
    print(num3,"is greater among all ")

else :
    print ("Numbers are equal")