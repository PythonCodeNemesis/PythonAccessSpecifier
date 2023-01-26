'''Outside class without object'''

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

        # NameError: name '_PrivateClass__multiply_by_3_private' is not defined
        # you cant use private function of private class from public function without object

        # y = __multiply_by_3_private(x)
        # return y

        return x*3


    def multiple_by_3_obj(self, x):
        y = self.__multiply_by_3_private(x)
        return y
    def _divide_by_3(x):
        y = x//3
        return y
    def __add_3(x):
        y = x//3
        return y


y = __PrivateClass.multiply_by_3(7) # public fn of private class
print(y)

# y = __PrivateClass.__add_3(77) # private fn of private class
# print(y)
# Gives Error : AttributeError: type object '__PrivateClass' has no attribute '__add_3'

y = __PrivateClass._divide_by_3(30) # protected fn of protected class
print(y)

