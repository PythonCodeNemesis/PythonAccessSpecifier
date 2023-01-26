# same class without object

class _ProtectedClass:
  def __init__(self, name, area_of_expertise):
    self.name = name
    self._area_of_expertise = area_of_expertise
  def _display_area_of_expertise(self):
    print(self._area_of_expertise)
  def multiply_by_3(x):
        y = x*3
        return y
  def _divide_by_3(x):
        y = x//3
        return y
  def __add_3(x):
        y = x//3
        return y

y = _ProtectedClass.multiply_by_3(7) # public fn of protected class
print(y)

# y = _ProtectedClass.__add_3(77) # private fn of protected class
# print(y)
# Gives Error : AttributeError: type object '_ProtectedClass' has no attribute '__add_3'

y = _ProtectedClass._divide_by_3(30) # protected fn of protected class
print(y)