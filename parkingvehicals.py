print("1.cars")
print("2.truck/bus")
print("3.bike/scooter/cycle")
vehical=int(input("Enter the vehical(car,truck/bus,bike/scooter/cycle)"))
intime=float(input("Enter in time: "))
outtime=float(input("Enter out time: "))
parking_hours=outtime-intime

if vehical==1:
    if parking_hours<=3:
        charges=10*parking_hours
    else:
        charges=20*parking_hours
    print("CHARGES YOU HAVE TO PAY=",charges)


elif vehical==2:
    if parking_hours<=3:
        charges=20*parking_hours
    else:
        charges=30*parking_hours
    print("CHARGES YOU HAVE TO PAY=",charges)

elif vehical==3:
    if parking_hours<=3:
        charges=5*parking_hours
    else:
        charges=10*parking_hours
    print("CHARGES YOU HAVE TO PAY=",charges)

else:
    print("INVALID VEHICAL CHOICE")

  