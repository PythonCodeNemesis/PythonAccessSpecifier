class PrivateClass:
    def __init__(self, name, area_of_expertise):
        self.name = name
        self.__area_of_expertise = area_of_expertise
    def __display_area_of_expertise_protected(self):
        print("Inside private function")
        print(self.__area_of_expertise)
    def display_area_of_expertise_public(self):
        print("Inside public function")
        self.__display_area_of_expertise_protected()

class DerivedClass(PrivateClass):
    def __init__(self, name, area_of_expertise):
        PrivateClass.__init__(self, name, area_of_expertise)
    def __display_area_of_expertise_from_derived_class(self):
        print(self.__display_area_of_expertise())    

obj1 = PrivateClass("Nemesis", "python")
obj1.display_area_of_expertise_public()

'''
when you execute the above two lines, you
see that you can call the public function 
of private function outside the private
class. The public function calls the private
function inside which prints a private data
member. This is how we can access private 
functions and data members outside private classes, by using
public functions.
'''

# obj1.__display_area_of_expertise_protected()

# The above line will give an error : AttributeError: 'PrivateClass' object has no attribute '__display_area_of_expertise'
# 

print(obj1.name)

# this is public data member so can be accessed outside

obj3 = DerivedClass("Nemesis", "python")
obj3.display_area_of_expertise_public()

# derived class can also access public function. Private function has been called from inside the public function so it has not been used outside the class.

obj3.__display_area_of_expertise()
print(obj3.name)

