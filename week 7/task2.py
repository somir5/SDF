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