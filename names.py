def main():
    boys_names = boys()
    girls_names = girls()
    pop_names(boys_names, girls_names)


def boys():
    boys_file = open('BoyNames.txt', 'r')
    boys_names = boys_file.readlines()
    index = 0
    while index < len(boys_names):
        boys_names[index] = boys_names[index].rstrip('\n')
        index += 1
    return boys_names


def girls():
    girls_file = open('GirlNames.txt', 'r')
    girls_names = girls_file.readlines()
    index = 0
    while index < len(girls_names):
        girls_names[index] = girls_names[index].rstrip('\n')
        index += 1
    return girls_names


def pop_names(boys, girls):
    user_name = input("Please enter a name.")
    if user_name in boys:
        print(user_name, "was one of the most popular boy names.")
    elif user_name in girls:
        print(user_name, "was one of the most popular girl names.")
    else:
        print("Pick a more popular name next time, bucko")

main()
