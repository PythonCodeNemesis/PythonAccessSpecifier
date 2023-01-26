# derived class without object

class PublicClass:
    def __init__(self, name, area_of_expertise):
        self.name = name
        self.area_of_expertise = area_of_expertise
    def display_area_of_expertise(self):
        print(self.area_of_expertise)
    def display_area_of_expertise_public(self):
        print(self.area_of_expertise)
    def __display_area_of_expertise_private(self):
        print(self.area_of_expertise)
    def _display_area_of_expertise_protected(self):
        print(self.area_of_expertise)


class DerivedClass(PublicClass):
    def __init__(self, name, area_of_expertise):
        PublicClass.__init__(self, name, area_of_expertise)
    def display_area_of_expertise_outside(self):
        print(self.display_area_of_expertise) 


obj1 = DerivedClass("Nemesis_1","python_public")
y = obj1.display_area_of_expertise_public() # public fn of public class

obj2 = DerivedClass("Nemesis","python_private")
y = obj2.__display_area_of_expertise_private() # private instance method of public class
print(y)

# Output : AttributeError: 'DerivedClass' object has no attribute '__display_area_of_expertise_private'

obj3 = DerivedClass("Nemesis_1","python_protected")
y = obj3._display_area_of_expertise_protected() # protected instance method of public class

# miscellaneous

# obj4 = DerivedClass("Gucci", "Perfume")
# obj4.display_area_of_expertise()
# print(obj4.name)
# print(obj4.multiply_by_3(10)) # so you cant do this as the first argument in this call is self, but this is not a object method.
