# wap that has a class Store which keeps a record of code and price
# of each product. display the menu of all products to the user and prompt him to enter 
# the quantity of each item required.and generate a bill and display total amount

class Store:
    def __init__(self):
        self.products = {'item1': 10, 'item2': 20, 'item3': 30, 'item4': 40}
        self.cart = {}

    def display_menu(self):
        print("===== Welcome to the Store =====")
        print("Code   |   Product   |   Price")
        print("-----------------------------")
        for code, price in self.products.items():
            print(f"{code}      |   {code.capitalize()}   |   ${price}")
        print("-----------------------------")

    def take_order(self):
        while True:
            code = input("Enter the product code (or 'done' to finish): ").lower()
            if code == 'done':
                break

            if code in self.products:
                quantity = int(input(f"How many {code.capitalize()} would you like to buy? "))
                self.cart[code] = quantity
            else:
                print("Invalid product code. Please try again.")

    def generate_bill(self):
        total_amount = 0
        print("\n===== Your Bill =====")
        for code, quantity in self.cart.items():
            price = self.products[code]
            total_price = price * quantity
            print(f"{code.capitalize()} x{quantity}: ${total_price}")
            total_amount += total_price
        print("-----------------------------")
        print(f"Total Amount: ${total_amount}")

    def run_store(self):
        self.display_menu()
        self.take_order()
        self.generate_bill()


# Create an instance of the Store class and run the store
store_instance = Store()
store_instance.run_store()
