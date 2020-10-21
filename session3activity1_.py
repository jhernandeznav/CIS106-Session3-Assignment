# This program is for activity
def get_name():
    print("What is your name? ")
    name = input()
    return name


def display_result(name):
    print("Hello", str(name), "!")


def main():
    name = get_name()
    display_result(name)


main()
