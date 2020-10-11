
item_num = int(input("Please enter the number of items on your grocery  list.\n"))
item_price = [float(input("Enter the price of the item \n")) for i in range(item_num)]
item_quan = [int(input("What is the quantity of item #" + str(count + 1) + " that you bought?\n"))
             for count in range(item_num)]
subtotal = sum(float(quan * price) for quan, price in zip(item_quan, item_price))
print("The subtotal is", subtotal)
tax = 0.07 * subtotal
total = subtotal + tax
print("The grand total is", total)
