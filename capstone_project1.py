basket_total_price = 0
shopping_basket = [{'cat food': 2}, {'dog food': 2}]
store_products = []
animal_products = [
    "cat food", "dog food", "cat toy",
    "dog toy", "ball", "collar",
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
def show_store_items(list):
    """ display the items in the store and their prices upon request"""

    print('+'*79)
    print(f"View our {len(list)} products:\n")
    for product in list: 
        for prod_info, prod_price in product.items():
            print(f"Product: {prod_info}\nPrice: £{prod_price}\n")
    print('+'*79)
show_store = show_store_items(store_products)

def total_cart(arg1, arg2):
    pass

# display the users shopping basket once they add items.
def display_user_shopping_basket(list):

    if len(list) < 1:
        print("You have no items in your cart")
    else:
        print("Your shopping cart:\n")
        for item in list:
            print(item)


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


print(shopping_basket)

def remove_from_cart(user_basket):

    finished_removing = False

    while (not finished_removing):
        
        quit_loop = input("Select q to exit or enter any key to contiue: ")

        if quit_loop == 'q':
            finished_removing = True
            print("You will return to the main menu")
        else:
            if len(user_basket) == 0:
                finished_removing = True
                print("Your basket is empty.")
            else:   
                print("Here are the item in your basket:")
                for index, item in enumerate(user_basket, 1): # start index from pos 1
                    print(index, item)

                user_input = len(input("Enter the number of the product you want to REMOVE: "))
                user_basket.pop(user_input - 1) # subtract 1 from user input so that the user can delete the correct index item.
    print('-'*79)             
    # loop through the basket to remove an item
    # added functionality will include totaling the basket, may require extra param for basket total
    # user can continuously remove items from the basket by choosing which item to remove by position
    # if the length of the basket is 0 break the loop and inform the user, basket is empty


# all live variables
# show_basket = display_user_shopping_basket(shopping_basket)
# user_add_item = add_to_cart(shopping_basket, store_products)
remove_product = remove_from_cart(shopping_basket)


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
