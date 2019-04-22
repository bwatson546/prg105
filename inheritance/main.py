import officefurniture
import desk


def main():
    generic = officefurniture.OfficeFurniture("nondescript", "furniture product", "material", "an amount of", "some", "a non-zero serving of", 1.11)

    desk_item = desk.Desk("beautiful", "desk", "wood", "thirty", "one hundred", "fifty", 15.00, "left", "three")

    print(generic)
    print(desk_item)


main()
