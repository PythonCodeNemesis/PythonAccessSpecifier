class ProtectedClass:
  def __init__(self, name, area_of_expertise):
    self.name = name
    self._area_of_expertise = area_of_expertise
  def _display_area_of_expertise(self):
    print(self._area_of_expertise)

class DerivedClass(ProtectedClass):
    def __init__(self, name, area_of_expertise):
        ProtectedClass.__init__(self, name, area_of_expertise)
    def display_area_of_expertise_outside(self):
        print(self._display_area_of_expertise)    



obj3 = DerivedClass("Nemesis", "python")
obj3._display_area_of_expertise()
print(obj3._area_of_expertise)

obj4 = DerivedClass("Gucci", "Perfume")
obj4._display_area_of_expertise()
print(obj4._area_of_expertise)

obj1 = ProtectedClass("Nemesis", "python")
obj1._display_area_of_expertise()
print(obj1._area_of_expertise)

obj2 = ProtectedClass("Gucci", "Perfume")
obj2._display_area_of_expertise()
print(obj2._area_of_expertise)