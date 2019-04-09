import pickle

#  choices
LOOKUP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5


def main():
    try:
        input_file = open("customer_file.dat", "rb")
        customers = pickle.load(input_file)
    except (FileNotFoundError, IOError):
        print("FILE NOT FOUND. PLEASE ADD A CUSTOMER AND THEN QUIT TO CREATE THE FILE.")
        customers = {}
    #  Initialize a variable for menu selections
    choice = 0

    while choice != QUIT:
        #  get the choice
        choice = menu()

        #  choice machine
        if choice == LOOKUP:
            look_up(customers)
        elif choice == ADD:
            add(customers)
        elif choice == CHANGE:
            change(customers)
        elif choice == DELETE:
            delete(customers)
        elif choice == QUIT:
            save(customers)


def menu():
    print()
    print("CUSTOMER EMAIL LOOKUP")
    print("-----------------------")
    print("1. LOOK UP AN EMAIL ADDRESS")
    print("2. ADD A NEW CUSTOMER")
    print("3. CHANGE AN EMAIL ADDRESS")
    print("4. DELETE A CUSTOMER")
    print("5. QUIT THE PROGRAM\n")
    #  get choice
    choice = int(input("Enter the number of your choice: "))
    while choice < 1 or choice > 5:
        choice = int(input("Enter the VALID number of your choice: "))
    return choice


#  LOOKUP
def look_up(customers):
    name = input("Enter a customer's name: ")
    print(customers.get(name, 'Not Found'))


#  ADD
def add(customers):
    name = input("Enter customer name: ")
    phone = input("Enter customer email address: ")
    if name not in customers:
        customers[name] = phone
        print("Customer created.")
    else:
        print("That entry already exists.")


#  CHANGE
def change(customers):
    name = input("Enter the customer name: ")
    if name in customers:
        phone = input("Enter the new email address: ")
        customers[name] = phone
        print("Customer added.")
    else:
        print("That customer is not found.")


#  DELETE
def delete(customers):
    name = input("Enter the customer name: ")
    if name in customers:
        del customers[name]
        print("Customer terminated.")
    else:
        print("That customer was not found.")


def save(customers):
    print("The data file has been updated with your changes.")
    save_file = open('customer_file.dat', 'wb')
    pickle.dump(customers, save_file)
    save_file.close()


main()
