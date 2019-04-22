import officefurniture


class Desk(officefurniture.OfficeFurniture):
    def __init__(self, descrip, category, material, length, width, height, price, location_of_drawers, number_drawers):
        officefurniture.OfficeFurniture.__init__(self, descrip, category, material, length, width, height, price)
        self.__location_of_drawers = location_of_drawers
        self.__number_drawers = number_drawers

    def set_location_of_drawers(self, location_of_drawers):
        self.__location_of_drawers = location_of_drawers

    def get_location_of_drawers(self):
        return self.__location_of_drawers

    def set_number_drawers(self, number_drawers):
        self.__number_drawers = number_drawers

    def get_number_drawers(self):
        return self.__number_drawers

    def __str__(self):
        desk_statement = "You've got a good eye! This" + str(self.__descrip), str(self.__category) + "has been getting a lot of lookers! It's made of solid " + str(self.__material) + "and you KNOW how that does. It's " + str(self.__length) + "inches long, and " + str(self.__width) + "inches wide, " + str(self.__height) + " inches tall, and we only use inches here because I'm not programmed to convert that into feet! But putting my existential crisis as a program made to repeat a paragraph aside, it also has " + str(self.__number_drawers) + " drawers on the " + str(self.__location_of_drawers) + " side, because it's a desk! This bad boy can be yours for " + format(self.__price, ",.2f") + ". What do you say?"
        return desk_statement
