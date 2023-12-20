year=int(input("Enter a year to check the leap year ="))
if (year%4==0 and year%100!=0) or year %400==0:
    print("The year is leap year")

else :
    print("The year is not leap year")