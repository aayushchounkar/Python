#WAP Arithmetic Operations and perform operation

a=int(input("Enter the First Number:"))
b=int(input("Enter the Second Number:"))

d=input("Enter the Arithmetic Operations\n(+,-,*,/,power):")
if(d=="+"):
    print("Sum of", a, "+", b,"=",a+b)
elif(d=="-"):
    print("Sub of", a, "-", b,"=",a-b)
elif(d=="*"):
    print("Multiplication of", a, "*", b,"=",a*b)
elif(d=="/"):
    print("Division of", a, "/", b,"=",a/b)
else:
    print(b,"to the power of", a,"is:",a**b)