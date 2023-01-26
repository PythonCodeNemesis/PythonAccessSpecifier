# same class with object

class _ProtectedClass:
  def __init__(self, name, area_of_expertise):
    self.name = name
    self._area_of_expertise = area_of_expertise
  def display_area_of_expertise_public(self):
    print(self._area_of_expertise)
  def __display_area_of_expertise_private(self):
    print(self._area_of_expertise)
  def _display_area_of_expertise_protected(self):
    print(self._area_of_expertise)

class DerivedClass(_ProtectedClass):
    def __init__(self, name, area_of_expertise):
        _ProtectedClass.__init__(self, name, area_of_expertise)
    def display_area_of_expertise_from_derived_class(self):
        print(self.display_area_of_expertise_public()) 
    def multiply_by_3_priv(x):
        y = _ProtectedClass.__multiply_by_3_private(x) #internally calls private function
        return y   
    def multiply_by_3_pub(x):
        y = _ProtectedClass.multiply_by_3(x) #internally calls public function
        return y  

obj1 = DerivedClass("Nemesis_1","python_public")
y = obj1.display_area_of_expertise_public() # public fn of protected class

# obj2 = DerivedClass("Nemesis","python_private")
# y = obj2.__display_area_of_expertise_private() # private instance method of protected class
# print(y)

# Output : AttributeError: 'DerivedClass' object has no attribute '__display_area_of_expertise_private'

obj3 = DerivedClass("Nemesis_1","python_protected")
y = obj3._display_area_of_expertise_protected() # protected instance method of protected class
  