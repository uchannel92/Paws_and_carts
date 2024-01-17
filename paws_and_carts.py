def read_basket_file():
    with open(filename, 'r') as file_obj:
        file_contents = file_obj.readlines()
    return file_contents

def format_store_file_contents():
    for line in file_contents:
        format_line_content = line.strip().replace(',', ' ').split()
        product_id = format_line_content[0] # item_n
        product_name = format_line_content[1].replace('_', ' ') # product name
        product_price = format_line_content[2] # product price
        product = [product_id, product_name, product_price]
        products.append(product) # here i populate the products list.

def populate_store_products_to_dict():
    for product_index, product in enumerate(products):
        product_id = products[product_index][0]
        product_name = products[product_index][1]
        product_price = products[product_index][2]
        products_dict[product_id] = [product_name, product_price]

def display_store_products_to_user():
    print("Our products:")
    for item, product in products_dict.items():
        for i in product:
            catalogue = f"Product Name: {product[0]}\nProduct Price: £{product[1]}"
            print(catalogue)
            break

def add_product():
    user_product_to_add_input = input("Enter what item you want to add: ")
    return user_product_to_add_input

def validate_user_product(add_item): # this param is the return value from the user add_product func
    for item in products:
        store_product = item[1] # we're focused only on product items index.
        if add_item == store_product:
            add_item = store_product
            print(f"Your product:{add_item} == {store_product}")
            return True
        
def obtain_product_and_price(add_item):
    for item, product in products_dict.items():
        for i in product: # i is refence to the title of the product.
            if i == add_item:
                prod, price = product[0], product[1]
                return f"{prod}, {price}" # return nested list of product and price.

def write_to_basket_file(add_item):
    print("Product has been added!")
    # def add_product() needs to be a value here, the return value from a successful product
    # basket.append() # the product variable from user
    # output - user item has been added to basket.
    filename = "user_basket.txt"
    with open(filename, 'a') as file_obj:
        print("Your item has been added to the basket.")
        file_obj.write(add_item)

# def read_basket_file():
#     filename = "user_basket.txt"
#     with open(filename, 'r') as file_obj:
#         file_contents = file_obj.readlines()
    
#     for item in file_contents:
#         print(item)

def display_products_in_user_basket():

    if len(basket) == 0:
        print("There are no items in your basket.")
    
    else:
        print("Here are the items in your basket.")
        # for product in basket:
        #     print(product)
        filename = "user_basket.txt"
        with open(filename, 'r') as file_obj:
            file_contents = file_obj.readlines()
    
        for item in file_contents:
            print(item)


basket = [] #["fish food", "£2"], ["collar", "£12"]
products_dict = {}
products = []
filename = "store_products_file.txt"

while True:
    file_contents = read_basket_file()
    format_store_file_contents()
    populate_store_products_to_dict()
    print(products)
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
        # read products from text file, format data, populate products into a dict, present products dict to user.
        display_store_products_to_user()
        break

    if user_input == '2':
        display_products_in_user_basket() # display the items the user has added to their basket.
        break

    if user_input == '3':
        add_item = add_product()
        if validate_user_product(add_item):
            item_to_add = obtain_product_and_price(add_item)
            write_to_basket_file(item_to_add)
            read_basket_file()
        else:
            print(f"{add_item} That item is not in our products list.")
        break

    if user_input == '4':
        break

    if user_input == '5':
        break

    if user_input == '6':
        break

    else:
        print("You have entered an incorrect menu value.")
        continue




# if user want to add an item to the basket, press option 2
# add_item = add_product()
# validate_user_product(add_item)

# def convert_products_from_file_to_dict(filename):
#     pass

# with open(filename, 'r') as file_obj:
#     for line in file_obj:
#         format_line = line.strip().replace(',', ' ').split()
#         products.append(format_line)

# print(products)

# for product_index, product in enumerate(products):
#     product_id = products[product_index][0]
#     product_name = products[product_index][1]
#     product_price = products[product_index][2]
#     products_dict[product_id] = [product_name, product_price]

# print(products_dict)
    
# file_contents = open_store_file_contents()
# format_store_file_contents()
# populate_store_products_to_dict()
# display_store_products()
# display_products_in_user_basket()
# for a user to add an item to the basket, the products list needs to be populated
