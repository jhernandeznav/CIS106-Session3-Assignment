
item_num = int(input("Please enter the number of items on your grocery list:\n"))
item_price = [float(input("Enter the price of the item: \n")) for i in range(item_num)]
item_quan = [int(input("What is the quantity of item #" + str(count + 1) + " that you bought?\n"))
             for count in range(item_num)]


def subtotal_purchase():
    subtotal = sum(float(quan * price) for quan, price in zip(item_quan, item_price))
    return subtotal


def tax_purchase():
    tax = 0.07 * subtotal_purchase()
    return tax


def total_purchase():
    total = subtotal_purchase() + tax_purchase()
    return total


print("Quantity: ", item_quan)
print("Price per item:$", item_price)


def display_subtotal(subtotal):
    print("Subtotal:$", subtotal)


def display_tax(tax):
    print("Tax:$", tax)


def display_total(total):
    print("Total cost:$", total)


def main():
    subtotal = subtotal_purchase()
    display_subtotal(subtotal)
    tax = tax_purchase()
    display_tax(tax)
    total = total_purchase()
    display_total(total)


main()
