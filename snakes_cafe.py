# Attribute: Stack Overflow and Kassie Bradshaw
menu = {
    "Wings": 0,
    "Cookies": 0,
    "Spring Rolls": 0,
    "Salmon": 0,
    "Steak": 0,
    "Meat Tornado": 0,
    "A Literal Garden": 0,
    "Ice Cream": 0,
    "Cake": 0,
    "Pie": 0,
    "Coffee": 0,
    "Tea": 0,
    "Unicorn Tears": 0,
}

def welcome():

    print('**************************************')
    print('**Welcome to the Snakes Cafe!**\n **Please see our menu below.** \n** To quit at any time, type "quit"**')
    print('**************************************')

def user_prompt():
    print('**************************************')
    print("** What would you like to order?  **")
    print('**************************************')

# # https://stackoverflow.com/questions/47207495/python-printing-dictionary-key-and-value-side-by-side
#
# def show_menu():
#     for key, value in menu.items():
#             print("{}, {}".format(key, value))

def show_menu():
    for key in menu.keys():
        print(key)


welcome()
user_prompt()
show_menu()
item = input('> ')
order = {}

while item.lower() != 'quit'.lower():
    if item.lower() not in [key.lower() for key in menu.keys()]:
        print('Invalid order, please order from the menu or type "quit"')
        item = input('> ')

    if item.lower() in [key.lower() for key in menu.keys()]:
        if item.lower() not in [key.lower() for key in order.keys()]:
            order[item] = 0
            order[item.lower()] += 1
            print(f" {order[item.lower()]} order of {item.lower()} has been added!")
            item = input('> ')

if item.lower() == 'quit'.lower():
    if order == {}:
        print('Sorry if you could not find what you wanted. Good day!')
    else:
        print(f" Your order of {order.values()} {order.keys()} will be served. ")














