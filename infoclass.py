#  defining the base class
class info:
    def __init__(self, name, address, age, phone):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

#  mutators
    def set_name(self, sname):
        self.name = sname

    def set_address(self, saddress):
        self.address = saddress

    def set_age(self, sage):
        self.age = sage

    def set_phone(self, sphone):
        self.phone = sphone

#  accessors
    def get_name(self):
        return self.name

    def get_address(self):
        return self.address

    def get_age(self):
        return self.age

    def get_phone(self):
        return self.phone

#  objectifying me + my peeps
Brandon = info('Brandon Watson', '317 S State St', 27, '779-777-6865')
Matt = info('Matt Grydzuk', '777 Lucky Boy Lane', 21, '814-382-5555')
Cara = info('Cara Darnell', '317 S State St', 26, '999-111-0000')

print('DETECTIVE MCGRUFF\'S SUSPECT REPORT')
print('------------------------------')
print('PRIMARY SUSPECT')
print('NAME:', Brandon.get_name())
print('LOCATION:', Brandon.get_address())
print('AGE:', Brandon.get_age())
print('PHONE:', Brandon.get_phone())
print('------------------------------')
print('ACCOMPLICE 1')
print('NAME:', Matt.get_name())
print('LOCATION:', Matt.get_address())
print('AGE:', Matt.get_age())
print('PHONE:', Matt.get_phone())
print('------------------------------')
print('ACCOMPLICE 2')
print('NAME:', Cara.get_name())
print('LOCATION:', Cara.get_address())
print('AGE:', Cara.get_age())
print('PHONE:', Cara.get_phone())


