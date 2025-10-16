item_id_counter = 0
def add_inventory_item():
    global item_id_counter
    item_name = input("Enter Item Name:")
    quantity = float(input("Enter quantity:"))
    price_per_item = float(input("Enter price per item in $: "))
    item_id_counter += 1
    item_id = item_id_counter

    item = {
        "Item ID": item_id,
        "Item Name":item_name,
        "Quantity": quantity,
        "Price per Item in $" : price_per_item
    }
    return item
new_item = add_inventory_item()
print("\nitem Added Successfully:")
print(new_item)

def calculate_total_value():
    item = add_inventory_item()
    total_value = item["Quantity"] * item["Price per Item in $"]
    return{
        "Item ID": item["Item ID"],
        "Item Name": item["Item Name"],
        "Quantity": item["Quantity"],
        "Price per Item in $": item["Price per Item in $"],
        "Total Value": total_value
    }
new_item = calculate_total_value()
print("item added Successfully with Total Value;")
print(new_item)

#Task 3

inventory = {}
def update_inventory(item_id):
    global inventory

    if item_id in inventory:
        print(f"Current details: {inventory[item_id]}")
        new_quantity = float(input("Enter new Quantity: "))
        new_price = float(input("Enter new Price per Item in $: "))

        #update the values
        inventory[item_id]["Quantity"] = new_quantity
        inventory[item_id]["Price per Item in $"] = new_price

        #update total value too
        inventory[item_id]["Total Value"] = new_quantity * new_price

        return f"Item{item_id} updated successfully! New details;{inventory[item_id]}"
    else:
        return f"Item with ID {item_id} not found!"




    def display_inventory():
        if not inventory:
            print("Inventory is empty.")
            return
        print("\nCurrent Inventory:")
        for item_id, details in inventory.items():
            print(f"Item ID: {item_id}, Details: {details}")


