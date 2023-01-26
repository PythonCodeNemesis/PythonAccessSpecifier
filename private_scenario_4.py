# derived class with object

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

obj1 = DerivedClass("Nemesis_1","python_public")
y = obj1.display_area_of_expertise_public() # public instance fn of private class

# Output : NameError: name '_DerivedClass__PrivateClass' is not defined

# obj2 = DerivedClass("Nemesis","python_private")
# y = obj2.__display_area_of_expertise_private() # private instance method of private class
# print(y)

# Output : AttributeError: 'DerivedClass' object has no attribute '__display_area_of_expertise_private'

obj3 = DerivedClass("Nemesis_1","python_protected")
y = obj3._display_area_of_expertise_protected() # protected instance method of private class

#miscellaeous

obj = DerivedClass("Tim","Python ofc!!!")
obj.display_area_of_expertise_from_derived_class()

# with object we were able to access the private function of super class through publiv function of base class