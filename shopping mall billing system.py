def calculate_total(items):
    return sum(item['price'] * item['quantity'] for item in items)

def generate_bill(items, total):
    print("\n************ Supermarket Billing System ************")
    print("---------------------------------------------------")
    print("Item\t\tQuantity\tPrice\t\tTotal")
    print("---------------------------------------------------")
    
    for item in items:
        print(f"{item['name']}\t\t{item['quantity']}\t\t{item['price']}\t\t{item['price'] * item['quantity']}")
    
    print("---------------------------------------------------")
    print(f"Total: {total}")
    print("---------------------------------------------------")

def get_category_items(category):
    categories = {
        1: [
            {"name": "Milk (1L)", "price": 60},
            {"name": "Curd (1/2L)", "price": 30},
            {"name": "Butter Milk (1Ps)", "price": 15},
            {"name": "Ghee (1/2kg)", "price": 100},
            {"name": "Butter", "price": 150},
            {"name": "Cheese", "price": 200}
        ],
        2: [
            {"name": "Dal (1 kg)", "price": 60},
            {"name": "Oil (1L)", "price": 180},
            {"name": "Vinegar (1L)", "price": 50},
            {"name": "Boost (1kg)", "price": 200},
            {"name": "Salt Packet", "price": 30},
            {"name": "Coffee Powder", "price": 150}
        ],
        3: [
            {"name": "Apples (Kg)", "price": 180},
            {"name": "Grapes (1Kg)", "price": 80},
            {"name": "Orange (1Kg)", "price": 70},
            {"name": "Water Melon", "price": 200},
            {"name": "Banana (12pcs)", "price": 60},
            {"name": "Kiwi (2pcs)", "price": 150}
        ],
        4: [
            {"name": "Cashew (Kg)", "price": 800},
            {"name": "Kismis (1Kg)", "price": 500},
            {"name": "Pistha (Kg)", "price": 1700},
            {"name": "Badam", "price": 1000}
        ],
        5: [
            {"name": "Fan", "price": 2800},
            {"name": "Tube Light", "price": 300},
            {"name": "Headsets", "price": 1700},
            {"name": "Speakers", "price": 1000}
        ]
    }
    return categories.get(category, [])

def supermarket_billing():
    print("WELCOME TO SUPERMARKET\n")
    
    items = []

    while True:
        print("\nSelect a category:")
        print("1. Dairy Products")
        print("2. Groceries")
        print("3. Fruits & Vegetables")
        print("4. Dry Fruits")
        print("5. Electronics")
        print("0. Quit")

        category = int(input("Enter category number: "))

        if category == 0:
            break

        items_list = get_category_items(category)

        if not items_list:
            print("Invalid category number.")
            continue

        print("\nAvailable items:")
        for i, item in enumerate(items_list, start=1):
            print(f"{i}. {item['name']} - {item['price']}/-")

        while True:
            item_number = int(input("\nEnter item number (or 0 to quit this category): "))
            if item_number == 0:
                break
            if item_number < 1 or item_number > len(items_list):
                print("Invalid item number. Please try again.")
                continue
            quantity = int(input("Enter quantity: "))
            item = items_list[item_number - 1].copy()
            item['quantity'] = quantity
            items.append(item)

    if items:
        total = calculate_total(items)
        generate_bill(items, total)
    else:
        print("No items purchased.")

# Start the supermarket billing system
supermarket_billing()
