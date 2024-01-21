def shop_options():
    """
    This function is prompting the user to input their choice from a menu of options.
    The user's input is then returned as the value of the `user_input` variable.
    """
    user_input = input("Menu:\n"
                    "1: View Store items\n"
                    "2: View your basket\n"
                    "3: Add items to basket\n"
                    "4: Remove items from basket\n"
                    "5: Checkout\n"
                    "6: Exit\n"
                    ": ")
    return user_input

def read_file_contents(file):
    """
    The function `read_file_contents` reads the contents of a file and returns them
    as a list of lines.
    """
    filename = file
    with open(filename, 'r') as file_obj:
        content = file_obj.readlines()
    return content

def format_file_contents_and_store_in_product_dict(file_contents):
    """
    The function takes in file contents, formats them, and stores them in a
    dictionary.
    """
    for line in file_contents:
        remove_new_line = line.strip()
        store_content_as_list = remove_new_line.split(',')
        product_id = store_content_as_list[0]
        product_name = store_content_as_list[1].strip()
        product_price = int(store_content_as_list[2])
        store_products_dict[product_id] = [product_name, product_price]
    return store_products_dict

def store_file_contents_in_dict(formated_content, store_file_contents_in_dict):
    """
    The function takes formatted content and stores it in a dictionary with the
    product name as the key and a list of the product's attributes as the value.
    """
    for product in formated_content:
        store_file_contents_in_dict[product[0]] = [product[1], product[2]]
    return store_file_contents_in_dict

def display_products_to_user(store_products_dict):
    """
    The function `display_products` takes a dictionary of store products as input
    and prints the product ID, name, and price for each product.
    """
    print("See our products:\n")
    for key, value in store_products_dict.items():
        product_id = key
        product_name = value[0]
        product_price = value[1]

        print('-'*79)
        print(f"Product ID: {product_id}\nProduct: {product_name}\nPrice: £{product_price}")

user_basket = []
store_products_dict = {}
filename = 'store_products_file.txt'
file_data = read_file_contents(filename)
formatted_content = format_file_contents_and_store_in_product_dict(file_data)

# Loop starts here
shopping_finished = False
while (not shopping_finished):

    user_option = shop_options()
    
    if user_option == '1':
        print("You selected 'View store items'")
        display_products = display_products_to_user(store_products_dict)

    elif user_option == '2':
        print("Do something")

    elif user_option == '3':
        # the product first needs to be found in the values of a the dict.values to continue.
        # add items to a basket will first write the product to a text file
        print("Do something")

    elif user_option == '4':
        print("Do something")

    elif user_option == '5':
        print("Do something")

    elif user_option == '6':
        print("Goodbye.")
        shopping_finished = True
    
    else:
        print("You have entered an invalid option.")
