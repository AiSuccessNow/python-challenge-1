# Menu dictionary
menu = {    #Snarks
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Ginger Bread (2)": 0.99,
        "Granola bar": 1.99,
        "Diabetics Cookie ": 2.19,
        "Grandma's Choice": 2.49
    },      #meals
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Teriyaki Beaf": 10.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99,
            "Double Vegan":10.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49,
            "Turkey": 10.49,
            "Plant Based": 12.99
        }
    },          #Drinks
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99,
            "Double Large":3.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49,
            "Orange Pekoe": 1.19
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced Coffee": 3.49,
            "Caramel Heaven": 5.49
        },
        "Bottled Water":{
            "Premium": 2.49,
            "Ragolis": 1.99,
            "Goya": 1.49,
           
        }
    },          #Desserts{}
    "Dessert": {
        "Chocolate cake": 10.99,
        "Cheesecake": {
            "Japanese": 7.49,
            "Strawberry": 6.49,
            "New York": 4.99,

        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49,
        "Short Bread Fav.": 5.99
    },
    "Smoothies": {
       "Tropical Heavens": 10.99,
       "Avocado Delite": 9.99,
       "Papaya_Mango Delite": 9.99
    }
}

menu_dashes = "-" * 42

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order = []

# Launch the store and present a greeting to the customer
print("\nWelcome to JOJO'S MOBILE KITCHEN.")


# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True 
while place_order:
    # Ask the customer from which menu category they want to order
    print("\nHow May We Serve You Today? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Enter your menu number here: ")

    # Check if customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You have chosen {menu_category_name}! \n")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
           
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }   
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }    
                    i += 1
            # 2. Ask customer to input menu item number
            menu_item_number = input("Please Enter Your Menu Item Number ")

            # 3. Check if the customer typed a number
            if menu_item_number.isdigit():
                
            # Convert the menu selection to an integer
                menu_item_number = int(menu_item_number)

            # 4. Check if the menu selection is in the menu items
            
            if menu_item_number in menu_items.keys():

            
                    # Store the item name as a variable
                    item_name = menu_items[menu_item_number]["Item name"]
            
                    # Ask the customer for the quantity of the menu item
                    
                    # Tell the customer that their input isn't valid
                
                    is_valid_amount = False
                    while not is_valid_amount:
                        quantity = input(f" \nHow many {item_name} would you like? ")
                        # Check if the quantity is a number, default to 1 if not
                        if not quantity.isdigit():
                            quantity = "1"
                            print("Your entry is not valid, please try again: \n")
                            print(f"How many {item_name} would you like to order today?: ")
                            is_valid_amount = False
                        else :
                            quantity = int(quantity)
                            is_valid_amount = True
                            # Add the item name, price, and quantity to the order list
                            order.append({
                                "Item Name":item_name,
                                "Price":menu_items[menu_item_number]["Price"],
                                "Quantity":quantity
                            })

                # Tell the customer they didn't select a menu option
            else:
                print("You did not select a valid menu option.")

        else:   
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} OOPS! Your selection is not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You did not select a number! \nDo you Wnat to try again?.")

    # 5. Check the customer's input

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input(f"\nAnything Else With Your {item_name} ? \nPlease Enter (Y)es or (N)o ")
        
        # Keep ordering
        if keep_ordering.upper() == "N":
            place_order = False
        
            # Since the customer decided to stop ordering, thank them for
                # their order
            print("Thank You My Friend for your order.")
        
            # Exit the keep ordering question loop
            break
        
        # Complete the order
        elif keep_ordering.upper() == "Y":
        
            # Exit the keep ordering question loop
            break
        
        # Tell the customer to try again
        else:
            print("Your Entry is NOT Valid. Please enter Y or N \n")

# Print out the customer's order
print(" \nSee what we are cooking for you ? .....YUMMY! \n")

# Uncomment the following line to check the structure of the order
#print(order)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
    
for each_dict in order:

    # 7. Store the dictionary items as variables
    item_name = each_dict["Item Name"]
    price = each_dict["Price"]
    quantity = each_dict["Quantity"]
    
    # 8. Calculate the number of spaces for formatted printing
    # 9. Create space strings
    after_item_name_spaces = " " * (28 - len(item_name))
    after_price_spaces = " " * (10 - len(str(price)))
 
    # 10. Print the item name, price, and quantity
    print(item_name + after_item_name_spaces, str(price) + after_price_spaces, quantity)

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
prices = sum([each["Price"] * each["Quantity"] for each in order])

print(f"\nSub Total is    $:{prices:.2f} ")
print(f"TOTAL DUE is:    $:{prices*1.1:.2f}  (Including 10% Taxes) \n")
print(f"We Appreciate Generous Tip of 10%, 15%, 20% or More :)")
print("How Would You Like To PayPay Today..? (CASH or DEBIT only Pls.) ")

print("\nThank You for Visiting JOJO's MOBILE KITCHEN. ")
print("Please Tell Your Friends About Our Amazing Kitchen. \nLet's Make It A GREAT Day :) OK? \n") 
