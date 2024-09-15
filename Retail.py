#Name: Hasin Shadab Rahman                                                          #UID:U87513234
class RetailItem:
    #An initializer to set the attributes Data members for name, amount, and price
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
    #A str method to format the output    
    def __str__(self):
        return f"{self.name.ljust(20)}{self.amount:^10}${self.price:.2f}"


def main():
    #Prompts user for number of items to enter
    num_items = int(input("How many items will you add today? "))
    #Validates at least 1 item is entered
    while num_items < 1:
        num_items = int(input("Invalid entry. Must add at least 1 item. How many items will you add today? "))
    #Stores items in a list    
    items = []
    
    for i in range(num_items):
        name = input(f"Name of item {i+1}: ")
        amount = int(input(f"Amount of item {i+1}: "))
        price = float(input(f"Price of item {i+1}: "))
        item = RetailItem(name, amount, price)
        items.append(item)
    #Prints a summary table of all items
    print("\nHere is a summary of the {} items you added:".format(num_items))
    print("Item".ljust(20), "Amount", "Price", sep='\t')
    print("-" * 40)
    for item in items:
        print(item)

if __name__ == "__main__":
    main()