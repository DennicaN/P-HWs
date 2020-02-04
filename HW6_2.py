class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def all_mass(self):
        asp_mass = 25
        thickness = 5
        result = (self._length * self._width * asp_mass * thickness) / 100
        print(f"Масса асфальта состовляет {result} тонн")


a = Road(20, 500)
a.all_mass()