
menu = {"Burger": 5.99,"Pizza": 8.99,"Salad": 4.99,"Coke": 1.50,
        "Ice Cream": 2.50}
def display_menu(): 
      print("--- Menu ---") 
      for item, price in menu.items():
          print(f"{item}: ${price}") 
def calculate_total(items):
    total = 0
    for item, quantity in items.items(): 
        total += menu[item] * quantity
    return total 
selected_items = {} 
display_menu()
while True:
    item = input("Enter item from the menu (or 'done' to finish): ")
    if item.lower() == 'done': 
     break
     if item in menu:
         quantity = int(input("Enter quantity: "))
         selected_items[item] = quantity
    else:
        print("Invalid item. Please select from the menu.") 
total_cost = calculate_total(selected_items)
print(f"Total cost: ${total_cost}")