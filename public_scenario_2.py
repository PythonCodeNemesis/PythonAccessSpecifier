# With object of same class

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

obj1 = PublicClass("Nemesis", "python")
obj1.display_area_of_expertise_public() # public function of public class
print(obj1.name)
print(obj1.area_of_expertise)

obj2 = PublicClass("Nemesis","python_private")
y = obj2.__display_area_of_expertise_private() # private instance method of protected class
print(y)

# Output : AttributeError: 'PublicClass' object has no attribute '__display_area_of_expertise_private'

obj3 = PublicClass("Nemesis_1","python_protected")
y = obj3._display_area_of_expertise_protected() # protected instance method of protected class