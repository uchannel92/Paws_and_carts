basket_total_price = 0
shopping_basket = []
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

def display_user_shopping_basket(list):

    if len(list) < 1:
        print("You have no items in your cart")
    else:
        print("Your shopping cart:\n")
        for item in list:
            print(item)

show_basket = display_user_shopping_basket(shopping_basket)

def add_to_cart():
    pass

def remove_from_cart():
    pass


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
