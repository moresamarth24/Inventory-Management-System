inventory = {}

def add_product():
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter initial quantity: "))

    inventory[name] = {
        "price": price,
        "quantity": quantity
    }
    print("✅ Product added successfully")

def update_stock():
    name = input("Enter product name: ")
    if name in inventory:
        qty = int(input("Enter quantity to add: "))
        inventory[name]["quantity"] += qty
        print("✅ Stock updated")
    else:
        print("❌ Product not found")

def sell_product():
    name = input("Enter product name: ")
    if name in inventory:
        qty = int(input("Enter quantity to sell: "))
        if qty <= inventory[name]["quantity"]:
            inventory[name]["quantity"] -= qty
            total_price = qty * inventory[name]["price"]
            print("💰 Sale completed | Total:", total_price)
        else:
            print("⚠️ Insufficient stock")
    else:
        print("❌ Product not found")

def view_inventory():
    print("\n📦 Current Inventory")
    for name, details in inventory.items():
        print(name, "| Price:", details["price"], "| Qty:", details["quantity"])

def inventory_menu():
    while True:
        print("\n----- INVENTORY MENU -----")
        print("1. Add Product")
        print("2. Update Stock")
        print("3. Sell Product")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            sell_product()
        elif choice == "4":
            view_inventory()
        elif choice == "5":
            print("👋 Exiting Inventory System")
            break
        else:
            print("❌ Invalid choice")

inventory_menu()
