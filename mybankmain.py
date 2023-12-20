import mybank

user = mybank.Banking()
while True:
    print("1.Withdraw")
    print("2.deposit")
    print("3.Checkbalance")
    print("4.Exit")
    choice=int(input("Enter your choice"))
    if choice==3:
        user.checkbalance()
        
    elif choice==2:
        takeamt=int(input("Enter amount you want to deposit"))
        user.deposit(takeamt)

    elif choice==1:
        withdrawamt=int(input("Enter amount you want to withdraw"))
        user.withdraw(withdrawamt)
    elif choice==4:
        print("Thankyou for banking with us")
        break 
