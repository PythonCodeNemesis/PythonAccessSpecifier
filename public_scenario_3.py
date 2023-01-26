# derived class without object

class PublicClass:
    def __init__(self, name, area_of_expertise):
        self.name = name
        self.area_of_expertise = area_of_expertise
    def display_area_of_expertise(self):
        print(self.area_of_expertise)
    def multiply_by_3(x):
        y = x*3
        return y
    def _divide_by_3(x):
        y = x//3
        return y
    def __add_3(x):
        y = x//3
        return y

class DerivedClass(PublicClass):
    def __init__(self, name, area_of_expertise):
        PublicClass.__init__(self, name, area_of_expertise)
    def display_area_of_expertise_outside(self):
        print(self.display_area_of_expertise) 
    def multiply_by_3(x):
        return PublicClass.multiply_by_3(x)
    def _divide_by_3(x):
        return PublicClass._divide_by_3(x)
    def __add_3(x):
        return PublicClass.__add_3(x)

y = DerivedClass.multiply_by_3(7) # public fn of public class
print(y)

# y = DerivedClass.__add_3(77) # private fn of public class
# print(y)
# Gives Error : AttributeError: type object '_PublicClass' has no attribute '__add_3'

y = DerivedClass._divide_by_3(30) # protected fn of public class
print(y)


