menu = {'PIZZA': 40,
        'PASTA': 50,
        'BURGER': 60,
        'SALAD': 70,
        'COFFEE': 80}
print("WELCOME TO GLALAXY CAFE, HERE'S THE MENU: \n PIZZA : RS 40\n PASTA : RS 50\n BURGER : RS 60\n SALAD : RS 70\n "
      "COFFEE : RS 80")
order_total = 0
item_1 = input("Enter Your First Order You Want To Order = ")

if item_1 in menu:
    order_total+= menu[item_1]
    print(f"Order of {item_1} has been added")

else:
    print(f"Order item {item_1} is not available Yet Please order something else")

another_item = input("Do You Want To Add Another Item (YES/NO) ")
if another_item == 'YES' or another_item == 'yes':
    item_2 = input("Enter the Second Item You Want To Order = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Order of {item_2} has been added to your order")
    else:
        print(f"Order item {item_2} is not available")
print(f"The Total Price of Your order is {order_total}")

