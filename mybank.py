class Banking:    
    def __init__(self):
        self.balance = 10000

    def checkbalance(self):
        print("The balance in your account =",self.balance)

    def withdraw(self,withdrawamt):
        self.balance-=withdrawamt
        print(f"The balance = {self.balance}")

    def deposit(self, takeamt):
        self.balance+=takeamt
        print("The balance =",self.balance)

if __name__=="__main__":
    print("server down")
else:
    print("kuch toh gaya")