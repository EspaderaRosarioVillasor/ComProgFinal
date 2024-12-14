class ProductRecords:
    def __init__(self, product_id, name, product_description, price, quantity):
        self.product_id = product_id
        self.name = name
        self.product_description = product_description
        self.price = price
        self.quantity = quantity

    def update_quantity(self, new_quantity):
        """Update the stock quantity of the product."""
        self.quantity = new_quantity

    def get_total_value(self):
        """Calculate the total value of the product in stock."""
        return self.price * self.quantity

    def __str__(self):
        """Return a string representation of the product details."""
        return f"ID: {self.product_id}, Name: {self.name}, Description: {self.product_description}, Price: {self.price}, Quantity: {self.quantity}"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product_id, name, product_description, price, quantity):
        """Add a new product to the inventory."""
        product = ProductRecords(product_id, name, product_description, price, quantity)
        self.products.append(product)

    def update_product_quantity(self, product_id, new_quantity):
        """Update the stock quantity of a product."""
        for product in self.products:
            if product.product_id == product_id:
                product.update_quantity(new_quantity)
                print(f"Updated quantity for {product.name} to {new_quantity}.")
                return
        print("Product not found.")

    def display_all_products(self):
        """Display all products in the inventory."""
        if self.products:
            for product in self.products:
                print(product)
        else:
            print("No products in inventory.")

    def calculate_total_inventory_value(self):
        """Calculate and display the total value of all products in inventory."""
        total_value = sum(product.get_total_value() for product in self.products)
        print(f"Total inventory value: {total_value:.2f}")


def main():
    inventory = Inventory()

    while True:
        print("\nInventory Management System")
        print("1. Add product")
        print("2. Update number of stock")
        print("3. View all products")
        print("4. Calculate total inventory value")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            product_description = input("Enter product description: ")
            price = float(input("Enter product price: "))
            quantity = int(input("Enter product quantity: "))
            inventory.add_product(product_id, name, product_description, price, quantity)
            print(f"Product {name} added successfully.")

        elif choice == "2":
            product_id = input("Enter product ID to update: ")
            new_quantity = int(input("Enter new quantity: "))
            inventory.update_product_quantity(product_id, new_quantity)

        elif choice == "3":
            inventory.display_all_products()

        elif choice == "4":
            inventory.calculate_total_inventory_value()

        elif choice == "5":
            print("Exiting the Inventory Management System.")
            break

        else:
            print("Invalid option. Try again")

if __name__ == "__main__":
    main()
