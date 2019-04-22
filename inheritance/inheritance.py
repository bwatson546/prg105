import office_furniture
import desk


def main():
    generic = office_furniture.OfficeFurniture("nondescript", "furniture product", "material", "an amount of", "some", "a non-zero serving of", 1.11)

    desk_item = desk.Desk("beautiful", "desk", "wood", "thirty", "one hundred", "fifty", 15.00)

    print(generic)
    print(desk_item)


main()
