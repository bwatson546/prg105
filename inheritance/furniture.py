#  define class
class OfficeFurniture:
    def __init__(self, descrip, category, material, length, width, height, price):
        self.__descrip = descrip
        self.__category = category
        self.__material = material
        self.__length = length
        self.__width = width
        self.__height = height
        self.__price = price

    def set_descrip(self, descrip):
        self.__descrip = descrip

    def set_category(self, category):
        self.__category = category

    def set_material(self, material):
        self.__material = material

    def set_length(self, length):
        self.__length = length

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def set_price(self, price):
        self.__price = price

    def get_descrip(self):
        return self.__descrip

    def get_category(self):
        return self.__category

    def get_material(self):
        return self.__material

    def get_length(self):
        return self.__length

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_price(self):
        return self.__price

    def __str__(self):
        office_statement = "You've got a good eye! This " + str(self.get_descrip()) + " " + str(self.get_category()) + " has been getting a lot of lookers! It's made of solid " + str(self.get_material()) + " and you KNOW how that does. It's " + str(self.get_length()) + " inches long, and " + str(self.get_width()) + " inches wide, " + str(self.get_height()) + " inches tall, and we only use inches here because I'm not programmed to convert that into feet! But putting my existential crisis as a program made to repeat a paragraph aside, this bad boy can be yours for ${:0,.2f}".format(self.get_price()) + ". What do you say?"
        return office_statement
