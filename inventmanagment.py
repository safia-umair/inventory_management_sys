# Inventory Management System

# Product Class
class Product:
    def __init__(self, product_id, name, category, price, stock_quantity):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price
        self.stock_quantity = stock_quantity

# Inventory System Class
class InventorySystem:
    def __init__(self):
        self.products = {}
        self.users = {
            "admin": {"password": "admin123", "role": "Admin"},
            "user": {"password": "user123", "role": "User"}
        }
        self.logged_in_user = None

    # Login Method
    def login(self, username, password):
        if username in self.users and self.users[username]["password"] == password:
            self.logged_in_user = self.users[username]
            print(f"Logged in as {username} ({self.logged_in_user['role']})")
        else:
            print("Invalid username or password")

    # Logout Method
    def logout(self):
        self.logged_in_user = None
        print("Logged out.")

    # Add Product (Admin Only)
    def add_product(self, product_id, name, category, price, stock_quantity):
        if self.logged_in_user and self.logged_in_user["role"] == "Admin":
            self.products[product_id] = Product(product_id, name, category, price, stock_quantity)
            print("Product added successfully.")
        else:
            print("Only admins can add products.")

    # View Products
    def view_products(self):
        if not self.products:
            print("No products available.")
        else:
            for product in self.products.values():
                print(f"{product.product_id}: {product.name} | {product.category} | Price: {product.price} | Stock: {product.stock_quantity}")

    # Adjust Stock (Admin Only)
    def adjust_stock(self, product_id, amount):
        if self.logged_in_user and self.logged_in_user["role"] == "Admin":
            if product_id in self.products:
                self.products[product_id].stock_quantity += amount
                print("Stock updated.")
            else:
                print("Product not found.")
        else:
            print("Only admins can adjust stock.")

# Main Program
inventory = InventorySystem()

def main():
    while True:
        print("\n--- Inventory Management ---")
        print("1. Login")
        print("2. Logout")
        print("3. Add Product (Admin Only)")
        print("4. View Products")
        print("5. Adjust Stock (Admin Only)")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == "1":
            username = input("Username: ")
            password = input("Password: ")
            inventory.login(username, password)
        elif choice == "2":
            inventory.logout()
        elif choice == "3":
            if inventory.logged_in_user and inventory.logged_in_user["role"] == "Admin":
                product_id = input("Product ID: ")
                name = input("Name: ")
                category = input("Category: ")
                price = float(input("Price: "))
                stock_quantity = int(input("Stock Quantity: "))
                inventory.add_product(product_id, name, category, price, stock_quantity)
            else:
                print("Admin access required.")
        elif choice == "4":
            inventory.view_products()
        elif choice == "5":
            if inventory.logged_in_user and inventory.logged_in_user["role"] == "Admin":
                product_id = input("Product ID: ")
                amount = int(input("Amount to adjust (+/-): "))
                inventory.adjust_stock(product_id, amount)
            else:
                print("Admin access required.")
        elif choice == "6":
            print("Exiting system.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
