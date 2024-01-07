basket_total_price = 0
shopping_basket = [{'cat food': 2}, {'dog food': 2}, {'collar': 6}, {'bird seeds': 7}, {'door flap': 22},]
store_products = []
animal_products = [
    "Fish food", "hamster wheel", "door flap",
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
    print('='*79)


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
                total += prod_price
            
            print(f"{prod_info} - £{prod_price:.2f}")
        
        # total
        print('-'*30)    
        print(f"Total: £{total:.2f}")
        print('='*30)   
    
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
        print(f"{animal_products[list_value]} has been added to the basket!")
    else:
        print(f"We cannot find your item - {user_input}")
        print("return to the menu and check what we have in stock.")
        print("Also ensure the item you are looking for is spelt properly.")
    print('-'*79)
    return user_basket

def remove_from_cart(user_basket):

    is_removal_completed = False

    while (not is_removal_completed):
        
        quit_loop = input("Select q to exit or enter any key to contiue: ")

        if quit_loop == 'q':
            is_removal_completed = True
            print("You will return to the main menu")
        else:
            if len(user_basket) == 0:
                is_removal_completed = True
                print("There are no items in your basket.")
            else:   
                print("Here are the item in your basket:")
                for index, item in enumerate(user_basket, 1): # start index from pos 1
                    print(index, item)

                # When removing the item from the list, i also need to remove the price from poped item so total is updated..
                # use method is.numeric() to check if value added is an integer, if not ask again..
                user_input = len(input("Enter the number of the product you want to REMOVE: "))
                user_basket.pop(user_input - 1) # subtract 1 from user input so that the user can delete the correct index item.
    print('-'*79)             
    # loop through the basket to remove an item
    # added functionality will include totaling the basket, may require extra param for basket total
    # user can continuously remove items from the basket by choosing which item to remove by position
    # if the length of the basket is 0 break the loop and inform the user, basket is empty


# all live variables
# print(shopping_basket)
# show_store = show_store_items(store_products)
show_basket = display_user_shopping_basket(shopping_basket)
# user_add_item = add_to_cart(shopping_basket, store_products)
# remove_product = remove_from_cart(shopping_basket)
# check_total = total_cart(basket_total_price, shopping_basket)

"""# Serge logic
shopping_done = False
while (not shopping_done):

    if 'x' == 'something':
        shopping_done = True
        print("Goodbye")
    pass

# Riaan logic
user_input = ''

while user_input != 'q':

    if user_input == 'q':
        break"""
