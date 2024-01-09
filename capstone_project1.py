basket_total_price = 0
# shopping_basket = [{'cat food': 2}, {'dog food': 2}, {'collar': 6}, {'cuen': 66}, {'bird seeds': 7}, {'door flap': 22},]
shopping_basket = []
store_products = []
animal_products = [
    "fish food", "hamster wheel", "door flap",
    "bowl", "bird seeds", "collar",
]
animal_products_price = [
    2, 3, 20, 22,
    7, 6
]

for list_value in range(len(animal_products)):

    store_items = {
        animal_products[list_value]: animal_products_price[list_value],
    }
    store_products.append(store_items)   

# display the available store items    
def show_store_items(store_list):
    """ display the items in the store and their prices upon request"""

    # header
    print('='*30)
    print(f"View our {len(store_list)} products:\n")
    print('='*30)

    # items
    print("Products")
    print('='*30)
    for product in store_list: 
        for prod_info, prod_price in product.items():
            print(f"{prod_info} -------- Price: £{prod_price}\n")

def total_cart(total, basket):

    if len(basket) == 0:
        print('There are no items in your basket')
        print('You will now return to the main menu')
    
    else:

        # Header
        print('='*30)
        print("Your Recipt:")
        print('='*30)

        # items
        for product in basket:
            for prod_info, prod_price in product.items():
                # print(prod_info)
                total += prod_price
            
            print(f"{prod_info} - £{prod_price:.2f}")
        
        # total
        print('-'*30)    
        print(f"Total: £{total:.2f}")
        print('='*30)
        print(f"\nYou will be emailed shortly to confirm payment details")   
    
# display the users shopping basket once they add items.
def display_user_shopping_basket(user_basket):

    if len(user_basket) < 1:
        print("You have no items in your cart")
    else:
        print("Your shopping cart:\n")
        for item in user_basket:
            print(item)
"""
UPDATE **** This for loop to display the shopping cart items with the correct format
            Loop again using the key and values to get the data listed nicely.
"""


# add a product listed in stock into the basket
def add_to_cart(user_basket, store_stock):

    item_found = False 
    user_input = input("Enter the name of the product you want to ADD: ")
    item_to_buy = ''
    for product in store_stock:
        if user_input in product.keys():
            item_to_buy = product
            item_found = True # once an item is found in stock break the loop
            break
    
    if item_found: #if true add the item to the user basket
        user_basket.append(item_to_buy)
        print(f"{user_input} has been added to the basket!")
    else:
        print(f"We cannot find your item - {user_input}")
        print("return to the menu and check what we have in stock.")
        print("Also ensure the item you are looking for is spelt properly.")

    return user_basket

# Remove an item from the cart
def remove_from_cart(total, user_basket):

    if len(user_basket) == 0:
        print('There are no items in your basket, you will return to the menu')
    else:
        is_removal_completed = False
        product_to_find = input("Enter the name of the product you want to REMOVE: ")
        found_product_price = ''
        found_product_index = ''

        # loop over user basket
        for basket_index, products in enumerate(user_basket):

            # obtain the index of the located dict. Use the dict key to obtain the value
            if product_to_find in products:
                found_product_index = basket_index
                found_product_price = user_basket[basket_index][product_to_find] # value of the dict key
                is_removal_completed = True
                break
            else:
                continue
        
        # remove dict from user basket and subtract linked price from the total
        if is_removal_completed == True:
            user_basket.pop(found_product_index)
            print(f"{product_to_find} - has been removed.")
            total -= found_product_price # remove the product price from the total
        else:
            print(f"Item '{product_to_find}' is not found in your basket")
            print('View your basket and check your products')
    
        return user_basket

shopping_done = False
print("*---* Welcome to the Paws & Cats *---*")
while (not shopping_done):
    
    user_input = input("Menu:\n"
                      "Option 1: View Store items\n"
                      "Option 2: View your basket\n"
                      "Option 3: Add items to basket\n"
                      "Option 4: Remove items from basket\n"
                      "Option 5: Checkout\n"
                      "Option 6: Exit\n"
                      ": ")
    print('-'*79)
    
    if user_input == '1':
        show_store = show_store_items(store_products)
        
    elif user_input == '2':
        show_basket = display_user_shopping_basket(shopping_basket)
        
    elif user_input == '3':
        user_add_item = add_to_cart(shopping_basket, store_products)
        
    elif user_input == '4':
        remove_product = remove_from_cart(basket_total_price, shopping_basket)
        
    elif user_input == '5':
        check_total = total_cart(basket_total_price, shopping_basket)
        
    elif user_input == '6':
        print("Goodbye!\nWe hope you enjoyed your visit!")
        shopping_done = True
    else:
        print("Please enter a vaid menu option.")
    
    print('-'*79)
