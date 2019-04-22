import furniture


class Desk(furniture.OfficeFurniture):
    def __init__(self, descrip, category, material, length, width, height, price, location_of_drawers, number_drawers):
        furniture.OfficeFurniture.__init__(self, descrip, category, material, length, width, height, price)
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
        desk_statement = "You've got a good eye! This " + str(self.get_descrip()) + " " + str(self.get_category()) + " has been getting a lot of lookers! It's made of solid " + str(self.get_material()) + " and you KNOW how that does. It's " + str(self.get_length()) + "inches long, and " + str(self.get_width()) + "inches wide, " + str(self.get_height()) + " inches tall, and we only use inches here because I'm not programmed to convert that into feet! But putting my existential crisis as a program made to repeat a paragraph aside, it also has " + str(self.get_number_drawers()) + " drawers on the " + str(self.get_location_of_drawers()) + " side, because it's a desk! This bad boy can be yours for ${:0,.2f}".format(self.get_price()) + ". What do you say?"
        return desk_statement
