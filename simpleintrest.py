#Write a program to calculate simple interest for given principal amount, time and rate of interest.
p=int(input("Enter Principle "))
r=int(input("Enter rate of interest: "))
t=int(input("Enter time period: "))
si=float(p*r*t)/100
print('The simple interest is: ',si)
print('The amount is',si+p)