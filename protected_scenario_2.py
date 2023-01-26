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
  

obj1 = _ProtectedClass("Nemesis_1","python_public")
y = obj1.display_area_of_expertise_public() # public fn of protected class

# obj2 = _ProtectedClass("Nemesis","python_private")
# y = obj2.__display_area_of_expertise_private() # private instance method of protected class
# print(y)

# AttributeError: '_ProtectedClass' object has no attribute '__display_area_of_expertise_private'

obj3 = _ProtectedClass("Nemesis_1","python_protected")
y = obj3._display_area_of_expertise_protected() # protected instance method of protected class