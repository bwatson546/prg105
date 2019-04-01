def main():  # main function
    user_num = get_num()
    num_list = random()
    bigger(user_num, num_list)


def random():  # creates and returns a list of 20 random numbers
    import random
    num_list = [random.randrange(0, 101) for num in range(20)]
    return num_list


def get_num():  # gets and returns a number from a user, exception doesn't display message??
    user_num = int(input("Gimme a number between 1 and 100"))
    try:
        return user_num
    except ValueError:
        print("Why are we playing this game. Come on.")


def bigger(user, numlist):  # checks user number against random numbers, and shows all bigger random numbers
    for num in numlist:
        if num > user:
            print(num)


main()
