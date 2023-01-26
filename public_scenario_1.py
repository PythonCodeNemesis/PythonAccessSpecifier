# same class without object

class PublicClass:
    def __init__(self, name = "default_name", area_of_expertise = "default area of expertise"):
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
 
# NameError: name 'multiply_by_3' is not defined

# y = multiply_by_3(7)
# print(y)

y = PublicClass.multiply_by_3(7) # public function of public class
print(y)

# y = PublicClass.__add_3(77) # private function of public class
# print(y)
# Gives Error : AttributeError: type object 'PublicClass' has no attribute '__add_3'

y = PublicClass._divide_by_3(30) # protected function of public class
print(y)






