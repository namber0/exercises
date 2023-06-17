class Purchase:
    def __init__(self, name, number, price):
        self.name = name 
        self.number = number
        self.price = price
    
    def get_price(self, buy_number):
        if buy_number >= 10:
            print("You will need to pay {} VND.".format(self.price * buy_number * 0.9))
        elif buy_number >= 5:
            print("You will need to pay {} VND".format(self.price * buy_number * 0.95))
        else:
            print("You will need to pay {} VND".format(self.price * buy_number))

    def make_purchase(self, buy_number):
        if self.number - buy_number >= 0:
            self.number = self.number - buy_number
        else:
            return -1

            
product = Purchase("Banh mi", 10, 20000)
buy_number = int(input("Enter the number of product you want to buy: "))
if product.make_purchase(buy_number) == -1:
    print("Not enough purchase to buy")
else:
    product.get_price(buy_number)
