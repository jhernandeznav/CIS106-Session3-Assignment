# This program finds the area and perimeter of a rectangle
length = float(input('Enter the length of the rectangle: '))
width = float(input('Enter the width of the rectangle: '))


def calculate_area():
    return length * width


def calculate_perimeter():
    return 2 * (length + width)


print("Area = ", calculate_area())
print("Perimeter = ", calculate_perimeter())
