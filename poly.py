#polymorphism in programming is the ability of a method or a functionn to be used in multiple situations or places for different purposes.
#it can also be defined as the ability of a methods are  behaviour of an object they are hence performed by an object
#eat()



class Product:
    def __init__(self, name, price):
        self.name = name 
        self.price = price 

    def calculate_total_cost(self, quantity):
        return self.price * quantity

class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author
class toy(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.author = author

class Electronics(Product):
    def __init__(self, name, price, age_range):
        super().__init__(name, price)
        self.age_range = age_range

    def calculate_inventory_cost(item, quantity):
        return item.calculate_total_cost(quantity) 
        Book = Book ("python programming", 5000, "John Doe")
        Electronics = Electronics ("Robot", 1000, "3-6 years")
        print(calculate_inventory_cost())
    


# Example usage
if __name__ == "__main__":
    # Create instances of products
    book1 = Book("Python Programming", 25.99, "John Doe")
    Electronics1 = Electronics("Building Blocks", 15.99, "3-6 years")

    # Calculate total cost for buying multiple items
    quantity_book1 = 3
    quantity_Electronics1 = 2
    quantity_toy1 = 2


    total_cost_book1 = book1.calculate_total_cost(quantity_book1)
    total_cost_toy1 = toy1.calculate_total_cost(quantity_toy1)
    total_cost_Electronics1 = Electronics1.calculate_total_cost(quantity_Electronics1)

    # Print the details and total cost
    print("Book details:")
    print("Name:", book1.name)
    print("Price:", book1.price)
    print("Author:", book1.author)
    print("Total cost for", quantity_book1, "books:", total_cost_book1)

    print("\ntoy details:")
    print("Name:", toy1.name)
    print("Price:", toy1.price)
    print("Age Range:", toy1.age_range)
    print("Total cost for", quantity_toy1, "toy:", total_cost_toy1)
    
    print("\nElectronics details:")
    print("Name:", Electronics1.name)
    print("Price:", Electronics1.price)
    print("Age Range:", Electronics1.age_range)
    print("Total cost for", quantity_Electronics1, "Electronicss:", total_cost_Electronics1)





# I am tasked to delevlop an inventory management system for a retail store
# The system should be able to handle different types of prosucts and calculate 
# the total cost of purchasing a specified quantity of each product



class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_cost(self, quantity):
        return self.price * quantity

class InventoryManagementSystem:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def calculate_total_cost(self):
        total_cost = 0
        for product in self.products:
            total_cost += product.calculate_cost(product.quantity)
        return total_cost

# Example usage:
inventory_system = InventoryManagementSystem()

# Adding products
inventory_system.add_product(Product("Apples", 1.5, 10))
inventory_system.add_product(Product("Bananas", 2, 5))
inventory_system.add_product(Product("Oranges", 1.8, 8))

# Calculating total cost
total_cost = inventory_system.calculate_total_cost()
print("Total cost of purchasing all products:", total_cost)






