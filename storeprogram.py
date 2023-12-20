# wap that has a class Store which keeps a record of code and price
# of each product. display the menu of all products to the user and prompt him to enter 
# the quantity of each item required.and generate a bill and display total amount

class Store:
    def __init__(self):
        self.products = {}

    def add_product(self, code, name, price):
        self.products[code] = {'name': name, 'price': price}

    def display_menu(self):
        print("Menu:")
        print("Code\tName\tPrice")
        for code, product in self.products.items():
            print(f"{code}\t{product['name']}\t₹{product['price']}")

    def generate_bill(self, order):
        total_amount = 0
        print("\nBill:")
        print("Code\tName\tPrice\tQuantity\tTotal")
        for code, quantity in order.items():
            product = self.products[code]
            item_total = quantity * product['price']
            total_amount += item_total
            print(f"{code}\t{product['name']}\t₹{product['price']}\t{quantity}\t\t₹{item_total}")

        print("\nTotal Amount: ₹".format(total_amount))


def main():
    store = Store()

    store.add_product('001', 'Bread', 10.99)
    store.add_product('002', 'Chips', 5.49)
    store.add_product('003', 'KitKat', 7.99)
    store.add_product('004', 'Coke', 10.99)
    store.add_product('005', 'Biscuit', 10.99)
    store.add_product('006', 'Butter', 10.99)
    store.add_product('007', 'Rice', 10.99)
    store.add_product('008', 'Lentils', 10.99)
    store.add_product('009', 'Suji', 10.99)
    store.add_product('010', 'Spice', 10.99)

    store.display_menu()

    order = {}
    while True:
        code = input("Enter the product code (or 'done' to finish): ")
        if code.lower() == 'done':
            break
        elif code in store.products:
            quantity = int(input(f"Enter the quantity for {store.products[code]['name']}: "))
            order[code] = quantity
        else:
            print("Invalid product code. Please enter a valid code.")

    store.generate_bill(order)


# if __name__ == “__main__”:
#     main()