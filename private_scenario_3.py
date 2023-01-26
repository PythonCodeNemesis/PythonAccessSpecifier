# derived class without object

class __PrivateClass:
    def __init__(self, name, area_of_expertise):
        self.name = name
        self.__area_of_expertise = area_of_expertise
    def __display_area_of_expertise_private(self):
        print("Inside private function")
        print(self.__area_of_expertise)
    def display_area_of_expertise_public(self):
        print("Inside public function")
        self.__display_area_of_expertise_private()
    def __multiply_by_3_private(x):
        y = x*3
        return y
    def multiply_by_3(x):
        y = __multiply_by_3_private(x)
        return y

class DerivedClass(__PrivateClass):
    def __init__(self, name, area_of_expertise):
        __PrivateClass.__init__(self, name, area_of_expertise)
    def display_area_of_expertise_from_derived_class(self):
        print(self.display_area_of_expertise_public()) 
    def multiply_by_3_priv(x):
        y = __PrivateClass.__multiply_by_3_private(x) #internally calls private function
        return y   
    def multiply_by_3_pub(x):
        y = __PrivateClass.multiply_by_3(x) #internally calls public function
        return y  

    def multiply_by_3(x):
        return __PrivateClass.multiply_by_3(x)
    def _divide_by_3(x):
        return __PrivateClass._divide_by_3(x)
    def __add_3(x):
        return __PrivateClass.__add_3(x)

# y = DerivedClass.multiply_by_3(7) # public instance method of private  class
# print(y)

# output : NameError: name '_DerivedClass__PrivateClass' is not defined

y = DerivedClass.__add_3(77) # private fn of private class
print(y)
# AttributeError: type object 'DerivedClass' has no attribute '__add_3'

# y = DerivedClass._divide_by_3(30) # protected fn of private class
# print(y)

# output : NameError: name '_DerivedClass__PrivateClass' is not defined

# print(DerivedClass.multiply_by_3_priv(60))
# AttributeError: type object 'PrivateClass' has no attribute '_DerivedClass__multiply_by_3_private'

# print(DerivedClass.multiply_by_3_pub(60))
# NameError: name '_PrivateClass__multiply_by_3_private' is not defined