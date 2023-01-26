'''Outside class with object'''

class __PrivateClass:
    def __init__(self, name, area_of_expertise):
        self.name = name
        self.__area_of_expertise = area_of_expertise
    def __display_area_of_expertise_protected(self):
        print("Inside private function")
        print(self.__area_of_expertise)
    def display_area_of_expertise_public(self):
        print("Inside public function")
        self.__display_area_of_expertise_protected()
    def __multiply_by_3_private(x):
        y = x*3
        return y
    def multiply_by_3(x):
        y = __multiply_by_3_private(x)
        return y


obj1 = __PrivateClass("Nemesis_1","python_public")
y = obj1.display_area_of_expertise_public() # public fn of private class

# obj2 = __PrivateClass("Nemesis_2","python_private")
# y = obj2.__display_area_of_expertise_private() # private instance method of private class

# AttributeError: '__PrivateClass' object has no attribute '__display_area_of_expertise_private'

obj3 = __PrivateClass("Nemesis_3","python_protected")
y = obj3._display_area_of_expertise_protected() # protected instance method of private class

# AttributeError: '__PrivateClass' object has no attribute '_display_area_of_expertise_protected'